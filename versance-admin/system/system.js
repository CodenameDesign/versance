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
