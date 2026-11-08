// usage: node proposals/render.js <dir>  -> <dir>/proposal.html to proposal.pdf + page-N.png previews; reports overflow
const {chromium}=require('playwright');const path=require('path');
(async()=>{const dir=path.resolve(process.argv[2]);const b=await chromium.launch();
const p=await b.newPage({viewport:{width:794,height:1123},deviceScaleFactor:2});await p.goto('file://'+dir+'/proposal.html');
await p.evaluate(()=>document.fonts.ready);
const pages=await p.$$('.page');
for(let i=0;i<pages.length;i++){const r=await pages[i].evaluate(n=>{const t=n.getBoundingClientRect(),c=n.querySelector('.content').getBoundingClientRect(),f=n.querySelector('.foot').getBoundingClientRect();return {bottom:Math.round(c.bottom-t.top),foot:Math.round(f.top-t.top)}});
 console.log('page',i+1,'content bottom',r.bottom,'foot top',r.foot,r.bottom>r.foot-12?'OVERFLOW':'ok');await pages[i].screenshot({path:dir+'/page-'+(i+1)+'.png'});}
await p.pdf({path:dir+'/Dr-Azka-Clinic-Growth-Proposal.pdf',format:'A4',printBackground:true,margin:{top:0,right:0,bottom:0,left:0}});
await b.close();})();
