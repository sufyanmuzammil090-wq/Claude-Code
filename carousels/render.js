// usage: node render.js <dir>  -> renders <dir>/slides.html to slide-XX.png, auto-fits headlines
const {chromium}=require('playwright');const path=require('path');
(async()=>{const dir=path.resolve(process.argv[2]);const b=await chromium.launch();
const p=await b.newPage({viewport:{width:1080,height:1400}});await p.goto('file://'+dir+'/slides.html');
await p.evaluate(()=>{document.querySelectorAll('h1').forEach(h=>{h.innerHTML='<span style="display:inline-block">'+h.innerHTML+'</span>';const s=h.firstChild;let fs=parseFloat(getComputedStyle(h).fontSize);while(s.offsetWidth*0.7>940&&fs>60){fs-=2;h.style.fontSize=fs+'px';}})});
const n=await p.$$eval('.slide',e=>e.length);
for(let i=1;i<=n;i++){const e=await p.$('#s'+i);const r=await e.evaluate(n=>{const t=n.getBoundingClientRect(),c=n.querySelector('.content').getBoundingClientRect();return Math.round(c.bottom-t.top)});console.log('slide',i,'content bottom',r,r>1250?'OVERFLOW':'ok');await e.screenshot({path:dir+'/slide-0'+i+'.png'});}
await b.close();})();
