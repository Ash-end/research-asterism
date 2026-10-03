// Optional browser regression for layout, navigation and the matrix content contract.
// Requires Playwright and a compatible browser; this does not assess scientific truth.
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const fs = require('fs');
const path = require('path');
const base = process.argv[2]?.replace(/\/$/, '');
const out = process.argv[3] && path.resolve(process.argv[3]);
if (!base || !out) throw new Error('Usage: node tests/site-check.cjs URL OUTPUT_DIRECTORY');
fs.mkdirSync(out, { recursive: true });
let browser;
const checks = [], errors = [], requests = [], links = [], widths = [];
function check(name, ok) { checks.push({ name, ok }); if (!ok) throw new Error(name); }
(async () => {
  const executablePath = process.env.BROWSER_EXECUTABLE;
  browser = await chromium.launch({ headless: true, ...(executablePath ? { executablePath } : {}) });
  const context = await browser.newContext({ viewport: { width: 1440, height: 1000 }, permissions: ['clipboard-read', 'clipboard-write'] });
  const page = await context.newPage();
  page.on('pageerror', error => errors.push(error.message));
  page.on('request', request => requests.push(request.url()));
  await page.goto(base + '/', { waitUntil: 'networkidle' });
  check('root redirect preserves project subpath', page.url() === base + '/site/');
  check('plain scientific title', (await page.title()).includes('研究问题、方法比较与证据评估'));
  const release = await (await context.request.get(base + '/release.json')).json();
  check('release version and date shown accurately', (await page.locator('#release-status').innerText()).includes('v' + release.version) && (await page.locator('#release-status').innerText()).includes(release.release_date));
  check('no unpublished-candidate status on landing', !(await page.locator('body').innerText()).includes('尚未公开更新'));
  check('constructed scenario disclaimer', (await page.locator('.scenario-status').innerText()).includes('非真实实验结果'));
  check('initial map visible', await page.locator('#panel-map').isVisible());
  check('three distinct mode tabs', await page.locator('[role=tab]').count() === 3);
  check('assumptions kept in separate table', await page.locator('#method-assumptions').count() === 1 && (await page.locator('#method-assumptions').innerText()).includes('假设'));
  check('strategies/mechanisms label and combinability', await page.locator('#method-assumptions th').first().innerText() === '策略/机制' && (await page.locator('#method-assumptions caption').innerText()).includes('这些策略可以组合，不构成互斥分类'));
  check('separate requirement and performance matrices', await page.locator('#requirements-matrix').count() === 1 && await page.locator('#performance-matrix').count() === 1);
  const cells = await page.locator('#performance-matrix td[data-evidence]').evaluateAll(elements => elements.map(element => ({ evidence: element.dataset.evidence, text: element.textContent.trim() })));
  check('all displayed synthetic estimates explicitly have no data', cells.length === 3 && cells.every(cell => cell.evidence === 'no-data' && cell.text === '无数据'));
  const performance = await page.locator('#performance-matrix tbody').innerText();
  check('performance cells contain no suitability assumptions or maintenance proxies', !/(缓慢漂移|噪声关系稳定|校准次数|切换次数|日光稳定)/.test(performance));
  check('evidence status has separate display', (await page.locator('.evidence-status').innerText()).includes('未提供'));
  await page.screenshot({ path: path.join(out, 'desktop.png'), fullPage: true });
  for (const mode of ['idea', 'result', 'map']) {
    await page.locator('#tab-' + mode).click();
    check('mouse selects ' + mode, await page.locator('#panel-' + mode).isVisible() && await page.locator('[role=tab][aria-selected=true]').count() === 1);
  }
  check('second mode uses validation design label', await page.locator('#panel-idea .next-step h4').textContent() === '验证设计');
  await page.locator('#tab-map').focus();
  await page.keyboard.press('ArrowRight'); check('ArrowRight selects next tab', await page.locator('#tab-idea').getAttribute('aria-selected') === 'true');
  await page.keyboard.press('End'); check('End selects final tab', await page.locator('#tab-result').getAttribute('aria-selected') === 'true');
  await page.keyboard.press('Home'); check('Home selects first tab', await page.locator('#tab-map').getAttribute('aria-selected') === 'true');
  await page.keyboard.press('ArrowLeft'); check('ArrowLeft wraps', await page.locator('#tab-result').getAttribute('aria-selected') === 'true');
  await page.locator('#tab-map').click();
  for (const id of ['install-code', 'prompt-code']) {
    await page.locator('#copy-status').evaluate(element => { element.textContent = ''; });
    await page.locator('[data-copy=' + id + ']').click();
    await page.waitForFunction(() => document.getElementById('copy-status').textContent.startsWith('已复制'));
    const copied = await page.evaluate(() => navigator.clipboard.readText());
    const expected = await page.locator('#' + id).textContent();
    check('clipboard exact content ' + id, copied.replace(/\r\n/g, '\n') === expected.replace(/\r\n/g, '\n'));
    if (id === 'install-code') {
      fs.writeFileSync(path.join(out, 'install-template.txt'), expected);
      check('installation uses manifest and refuses existing directory', expected.includes('release-files.json') && expected.includes("throw 'Target already exists'") && expected.includes("'.agents\\skills\\research-methodology'"));
    } else check('stable invocation', expected.includes('$research-methodology'));
  }
  // Simulate denied clipboard access to verify the explicit manual fallback.
  await page.evaluate(() => Object.defineProperty(navigator, 'clipboard', { configurable: true, value: undefined }));
  await page.locator('[data-copy=prompt-code]').click();
  check('clipboard fallback selects actual prompt', await page.evaluate(() => getSelection().toString() === document.getElementById('prompt-code').textContent));
  check('clipboard fallback informs user', (await page.locator('#copy-status').innerText()).includes('手动复制'));
  await page.evaluate(() => getSelection().removeAllRanges());
  for (const width of [320, 390, 768, 1440]) {
    await page.setViewportSize({ width, height: 844 });
    const size = await page.evaluate(() => ({ scroll: document.documentElement.scrollWidth, viewport: innerWidth }));
    widths.push({ width, ...size });
    check('landing no horizontal overflow at ' + width, size.scroll <= size.viewport);
    if (width === 390) {
      await page.evaluate(() => { document.activeElement.blur(); scrollTo(0, 0); });
      await page.screenshot({ path: path.join(out, 'mobile.png'), fullPage: true });
      await page.locator('#modes').screenshot({ path: path.join(out, 'mobile-modes.png') });
    }
  }
  await page.emulateMedia({ reducedMotion: 'reduce' });
  check('reduced motion disables smooth scroll', await page.evaluate(() => getComputedStyle(document.documentElement).scrollBehavior === 'auto'));
  const landing = await page.locator('a[href]').evaluateAll(elements => elements.map(element => element.href));
  await page.goto(base + '/site/docs.html', { waitUntil: 'networkidle' });
  for (const width of [320, 390, 768, 1440]) {
    await page.setViewportSize({ width, height: 844 });
    check('docs no horizontal overflow at ' + width, await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth));
  }
  check('docs version/date and published status', (await page.locator('main').innerText()).includes(release.release_date) && !(await page.locator('main').innerText()).includes('尚未公开更新'));
  check('three constructed examples in docs', await page.locator('details').count() === 3);
  await page.locator('summary').nth(1).click();
  check('docs disclosure opens', await page.locator('details').nth(1).getAttribute('open') !== null);
  const allLinks = [...landing, ...await page.locator('a[href]').evaluateAll(elements => elements.map(element => element.href))];
  const localLinks = allLinks.filter(href => new URL(href).origin === new URL(base).origin);
  check('documentation links stay inside project', localLinks.every(href => href.startsWith(base + '/')));
  for (const href of [...new Set(localLinks.map(href => href.split('#')[0]))]) {
    const response = await context.request.get(href);
    links.push({ url: href, status: response.status() });
  }
  check('all local linked resources reachable', links.every(link => link.status === 200));
  check('no browser errors', errors.length === 0);
  check('no external asset requests', requests.every(url => new URL(url).origin === new URL(base).origin));
  const nojs = await browser.newContext({ javaScriptEnabled: false, viewport: { width: 390, height: 844 } });
  const staticPage = await nojs.newPage();
  await staticPage.goto(base + '/site/');
  check('default scenario readable without JavaScript', await staticPage.locator('#panel-map').isVisible());
  check('other scenarios linked without JavaScript', await staticPage.locator('noscript a').isVisible());
  await nojs.close();
  fs.writeFileSync(path.join(out, 'results.json'), JSON.stringify({ scope: 'Browser behavior and explicit content contract; not scientific validity', browser: 'Chromium via Playwright', checks, widths, links, errors, externalRequests: requests.filter(url => new URL(url).origin !== new URL(base).origin) }, null, 2));
  console.log(JSON.stringify({ ok: true, checks: checks.length }));
})().catch(error => { console.error(error.stack); process.exitCode = 1; }).finally(async () => { if (browser) await browser.close(); });
