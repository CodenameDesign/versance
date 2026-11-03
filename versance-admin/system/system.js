(function(){var bar=document.querySelector('.bar');if(!bar)return;var burger=bar.querySelector('.bar__menu'),shut=bar.querySelector('.bar__close'),scrim=bar.querySelector('.bar__scrim'),wide=matchMedia('(min-width:901px)');
function set(o,focus){bar.classList.toggle('open',o);burger.setAttribute('aria-expanded',String(o));document.body.style.overflow=o?'hidden':'';if(focus)(o?shut:burger).focus();}
burger.addEventListener('click',function(){set(true,true);});shut.addEventListener('click',function(){set(false,true);});scrim.addEventListener('click',function(){set(false,true);});
document.addEventListener('keydown',function(e){if(e.key==='Escape'&&bar.classList.contains('open'))set(false,true);});
wide.addEventListener('change',function(){if(wide.matches&&bar.classList.contains('open'))set(false,false);});})();
document.addEventListener('click',function(e){
  var b=e.target.closest('.copy,[data-copy-text]');if(!b)return;
  var t=b.dataset.copyText||b.previousElementSibling.textContent;
  var old=b.textContent;
  (navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).catch(function(){
    var a=document.createElement('textarea');a.value=t;document.body.appendChild(a);a.select();try{document.execCommand('copy')}catch(x){}a.remove();});
  if(b.classList.contains('copy')){b.textContent='Copied';setTimeout(function(){b.textContent=old},1200);}
});
/* behind Mission Control's gate (the signed-in email is at /admin/whoami.json), a page of this system the person cannot open is left out of the menu: each link is asked for with a HEAD request and a 403 hides it */
(function(){var nav=document.getElementById('bar-nav');if(!nav||!window.fetch)return;
var root=document.documentElement,hostGated=/-mc[.]/.test(location.hostname),gated=hostGated;
try{if(sessionStorage.getItem('mc-gated'))gated=true;}catch(e){}
if(gated)root.classList.add('gating'); /* the links stay invisible until the answers are in, so none flashes before it is hidden */
var done=function(){root.classList.remove('gating');};setTimeout(done,3000);
var hide=function(){return Promise.all([].map.call(nav.querySelectorAll('a[href^="/admin/"]'),function(a){
    return fetch(a.getAttribute('href'),{method:'HEAD',credentials:'same-origin',cache:'no-store'}).then(function(r){if(r.status===403||r.status===401)a.hidden=true;}).catch(function(){});
  })).then(done);};
/* signed out on a gated host, the pages the gate would refuse are left out too (401) */
var signedOut=function(){try{sessionStorage.removeItem('mc-gated');}catch(e){}return gated?hide():done();};
fetch('/admin/whoami.json',{credentials:'same-origin',cache:'no-store'}).then(function(r){return r.ok?r.json():null;}).then(function(d){
  if(!d||!d.email)return signedOut();
  try{sessionStorage.setItem('mc-gated','1');}catch(e){}
  return hide();
}).catch(signedOut);})();
