'use strict';
const tabs = Array.from(document.querySelectorAll('[role="tab"]'));
function selectTab(tab, focus=false) {
  tabs.forEach(item => {const selected=item===tab;item.setAttribute('aria-selected',String(selected));item.tabIndex=selected?0:-1;document.getElementById(item.getAttribute('aria-controls')).hidden=!selected;});
  if(focus) tab.focus();
}
function selectHash(){const key=location.hash.slice(1);const tab=document.getElementById('tab-'+key);if(tab)selectTab(tab);}
selectHash();window.addEventListener('hashchange',selectHash);
tabs.forEach((tab,index)=>{tab.addEventListener('click',()=>selectTab(tab));tab.addEventListener('keydown',event=>{let next;if(event.key==='ArrowRight')next=(index+1)%tabs.length;if(event.key==='ArrowLeft')next=(index+tabs.length-1)%tabs.length;if(event.key==='Home')next=0;if(event.key==='End')next=tabs.length-1;if(next!==undefined){event.preventDefault();selectTab(tabs[next],true);}});});
document.querySelectorAll('[data-copy]').forEach(button=>button.addEventListener('click',async()=>{const element=document.getElementById(button.dataset.copy),status=document.getElementById('copy-status');try{if(!navigator.clipboard)throw new Error('Clipboard unavailable');await navigator.clipboard.writeText(element.textContent);status.textContent='已复制。请检查本地源码路径。';}catch(_){const range=document.createRange();range.selectNodeContents(element);const selection=window.getSelection();selection.removeAllRanges();selection.addRange(range);status.textContent='复制未获允许；文本已选中，可手动复制。';}}));
