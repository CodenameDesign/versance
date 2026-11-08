/* The pages by section and project, as Mission Control (Master Control) has them for this account. The list is Mission Control's
   own answer for the signed-in person, so it shows only what they may open. If it cannot be loaded (not signed in, a host with no
   gate, Mission Control down) the block stays hidden and the developer list below is all there is. Links are drawn only when they
   point at this same site, and are built with DOM calls, never from HTML strings. */
(function(){
  var box=document.getElementById("mc-structure");
  if(!box||!window.fetch)return;
  var src=box.getAttribute("data-src");
  if(!src)return;
  var OUT="M19 19H5V5h7V3H5c-1.11 0-2 .9-2 2v14c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2v-7h-2v7zM14 3v2h3.59l-9.83 9.83 1.41 1.41L19 6.41V10h2V3h-7z";
  function el(tag,cls,text){var e=document.createElement(tag);if(cls)e.className=cls;if(text!==undefined)e.textContent=text;return e;}
  function local(href){ /* the same-site path of a link, or null */
    try{var u=new URL(href,location.href);return u.origin===location.origin?u.pathname+u.search+u.hash:null;}catch(e){return null;}
  }
  function grid(pages){
    var ul=el("ul","mcgrid"),n=0;
    pages.forEach(function(p){
      var path=local(p.href);if(!path||typeof p.name!=="string")return;
      var a=el("a",null,null);a.href=path;a.target="_blank";a.rel="noopener";
      a.appendChild(el("span",null,p.name));
      var svg=document.createElementNS("http://www.w3.org/2000/svg","svg");svg.setAttribute("viewBox","0 0 24 24");svg.setAttribute("aria-hidden","true");
      var pa=document.createElementNS("http://www.w3.org/2000/svg","path");pa.setAttribute("d",OUT);svg.appendChild(pa);a.appendChild(svg);
      var li=el("li");li.appendChild(a);ul.appendChild(li);n++;
    });
    return n?ul:null;
  }
  fetch(src,{credentials:"include",cache:"no-store"}).then(function(r){return r.ok?r.json():null;}).then(function(d){
    if(!d||!Array.isArray(d.sections))return;
    var shown=0;
    d.sections.forEach(function(s){
      var sec=el("div","mcsec"),any=false;
      sec.id="sec-"+String(s.label).toLowerCase().replace(/[^a-z0-9]+/g,"-").replace(/^-+|-+$/g,""); /* the left nav links to it */
      sec.appendChild(el("h2",null,String(s.label)));
      var top=grid(s.pages||[]);if(top){sec.appendChild(top);any=true;}
      (s.projects||[]).forEach(function(p){var g=grid(p.pages||[]);if(g){sec.appendChild(el("h3",null,String(p.name)));sec.appendChild(g);any=true;}});
      if(any){box.appendChild(sec);shown++;}
    });
    if(shown){box.hidden=false;if(location.hash.length>1){var t=document.getElementById(location.hash.slice(1));if(t)t.scrollIntoView();}}
  }).catch(function(){});
})();
