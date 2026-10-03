// Browser behavior and explicit display contracts, not scientific validity.
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const fs = require('fs'), path = require('path');
const base=process.argv[2]?.replace(/\/$/,''), out=process.argv[3]&&path.resolve(process.argv[3]);
if(!base||!out)throw Error('Usage: node tests/site-check.cjs URL OUTPUT_DIRECTORY');
fs.mkdirSync(out,{recursive:true});
let browser;const checks=[], errors=[],requests=[],links=[],widths=[],anchors=[];
function check(name,ok){checks.push({name,ok});if(!ok)throw Error(name);}
(async()=>{
  browser=await chromium.launch({headless:true,...(process.env.BROWSER_EXECUTABLE?{executablePath:process.env.BROWSER_EXECUTABLE}:{})});
  const context=await browser.newContext({viewport:{width:1440,height:1000},permissions:['clipboard-read','clipboard-write']});
  const page=await context.newPage();page.on('pageerror',e=>errors.push(e.message));page.on('request',r=>requests.push(r.url()));
  const release=await(await context.request.get(base+'/release.json')).json();
  await page.goto(base+'/',{waitUntil:'networkidle'});
  check('root redirect preserves repository path',page.url()===base+'/site/');
  check('home title', (await page.title()).includes('研究问题、方法比较与证据评估'));
  check('version accurate',(await page.locator('#release-status').innerText()).includes('v'+release.version));
  check('short homepage separates deep examples',await page.locator('.cards article').count()===3 && await page.locator('#performance-matrix').count()===0);
  check('original guide accessible',await page.locator('a[href="handbook.html"]').count()>0);
  check('no full PDF embed',await page.locator('iframe,embed,object,a[href$=".pdf"]').count()===0);
  await page.screenshot({path:path.join(out,'desktop.png'),fullPage:true});
  for(const name of ['index.html','workflows.html','docs.html','handbook.html','evaluation.html']){
    await page.goto(base+'/site/'+name,{waitUntil:'networkidle'});
    check('one main landmark '+name,await page.locator('main').count()===1);
    check('one primary heading '+name,await page.locator('h1').count()===1);
    for(const width of [320,390,768,1440]){
      await page.setViewportSize({width,height:844});
      const size=await page.evaluate(()=>({scroll:document.documentElement.scrollWidth,viewport:innerWidth}));
      widths.push({page:name,width,...size});check('no horizontal overflow '+name+' '+width,size.scroll<=size.viewport);
      if(width===390&&name==='index.html')await page.screenshot({path:path.join(out,'mobile.png'),fullPage:true});
    }
    const hrefs=await page.locator('a[href]').evaluateAll(es=>es.map(e=>e.href));
    for(const href of hrefs.filter(h=>h.startsWith(base+'/'))){
      links.push(href.split('#')[0]);
      const url=new URL(href);
      if(url.hash&&url.pathname===new URL(page.url()).pathname){
        const id=decodeURIComponent(url.hash.slice(1));const ok=await page.locator('[id]').evaluateAll((es,id)=>es.some(e=>e.id===id),id);
        anchors.push({href,ok});check('same-page anchor '+name+' '+id,ok);
      }
    }
  }
  await page.goto(base+'/site/workflows.html#idea',{waitUntil:'networkidle'});
  check('deep link selects idea',await page.locator('#panel-idea').isVisible());
  for(const mode of ['map','result','idea']){await page.locator('#tab-'+mode).click();check('mouse tab '+mode,await page.locator('#panel-'+mode).isVisible()&&await page.locator('[role=tab][aria-selected=true]').count()===1);}
  check('validation design label',await page.locator('#panel-idea .next-step h4').innerText()==='验证设计');
  await page.locator('#tab-map').focus();await page.keyboard.press('ArrowRight');check('keyboard next',await page.locator('#tab-idea').getAttribute('aria-selected')==='true');
  await page.keyboard.press('End');check('keyboard End',await page.locator('#tab-result').getAttribute('aria-selected')==='true');
  await page.keyboard.press('Home');check('keyboard Home',await page.locator('#tab-map').getAttribute('aria-selected')==='true');
  await page.keyboard.press('ArrowLeft');check('keyboard wrap',await page.locator('#tab-result').getAttribute('aria-selected')==='true');
  await page.locator('#tab-map').click();
  check('strategy table preserves combinability',await page.locator('#method-assumptions th').first().innerText()==='策略/机制'&&(await page.locator('#method-assumptions caption').innerText()).includes('这些策略可以组合，不构成互斥分类'));
  check('requirements separate from performance',await page.locator('#requirements-matrix').count()===1&&await page.locator('#performance-matrix').count()===1);
  const cells=await page.locator('#performance-matrix td[data-evidence]').evaluateAll(es=>es.map(e=>({status:e.dataset.evidence,text:e.textContent.trim()})));
  check('conditional properties labeled',cells.length===3&&cells.every(c=>c.status==='derivation'));
  check('synthetic costs not measured',(await page.locator('#performance-matrix caption').innerText()).includes('不是实测'));
  await page.locator('#tab-idea').click();check('concrete method and cost',(await page.locator('#panel-idea').innerText()).includes('2+20/K')&&await page.locator('#panel-idea ol li').count()===3);
  await page.locator('#tab-map').click();
  check('evidence has separate display',(await page.locator('.evidence-status').innerText()).includes('未提供'));
  await page.setViewportSize({width:1440,height:1000});await page.screenshot({path:path.join(out,'workflows.png'),fullPage:true});
  await page.goto(base+'/site/docs.html',{waitUntil:'networkidle'});
  for(const id of ['install-code','prompt-code']){
    await page.locator('[data-copy='+id+']').click();await page.waitForFunction(()=>document.getElementById('copy-status').textContent.startsWith('已复制'));
    check('clipboard '+id,(await page.evaluate(()=>navigator.clipboard.readText())).replace(/\r\n/g,'\n')===(await page.locator('#'+id).textContent()).replace(/\r\n/g,'\n'));
  }
  check('bounded install documented',(await page.locator('#install-code').innerText()).includes('install_skill.py')&&(await page.locator('#install-code').innerText()).includes('--check'));
  await page.evaluate(()=>Object.defineProperty(navigator,'clipboard',{configurable:true,value:undefined}));await page.locator('[data-copy=prompt-code]').click();
  check('manual clipboard fallback',await page.evaluate(()=>getSelection().toString()===document.getElementById('prompt-code').textContent)&&(await page.locator('#copy-status').innerText()).includes('手动复制'));
  await page.locator('summary').nth(1).click();check('static disclosure works',await page.locator('details').nth(1).getAttribute('open')!==null);
  await page.emulateMedia({reducedMotion:'reduce'});check('reduced motion',await page.evaluate(()=>getComputedStyle(document.documentElement).scrollBehavior==='auto'));
  const resources=[];for(const href of [...new Set(links)]){const res=await context.request.get(href);resources.push({url:href,status:res.status()});}
  check('all local links reachable',resources.every(r=>r.status===200));
  check('no external asset requests',requests.every(url=>new URL(url).origin===new URL(base).origin));check('no script errors',errors.length===0);
  const nojs=await browser.newContext({javaScriptEnabled:false,viewport:{width:390,height:844}});const staticPage=await nojs.newPage();await staticPage.goto(base+'/site/workflows.html');
  check('default readable without JS',await staticPage.locator('#panel-map').isVisible());check('other scenarios have no-JS link',await staticPage.locator('noscript a').isVisible());await nojs.close();
  fs.writeFileSync(path.join(out,'results.json'),JSON.stringify({scope:'Browser behavior, layout and display contract; not scientific correctness',checks,widths,resources,anchors,errors},null,2));console.log(JSON.stringify({ok:true,checks:checks.length}));
})().catch(e=>{console.error(e.stack);process.exitCode=1;}).finally(async()=>{if(browser)await browser.close();});
