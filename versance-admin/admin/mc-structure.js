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
  function norm(p){return p.replace(/[/]+$/,"")||"/";}
  /* a section picked in the left nav (#sec-...) shows only that section: its block here, and below it only the developer rows for the same pages (the whole developer
     list is hidden if none of them is in this repo). No pick, or one that is not in the list, shows everything. */
  var h1=document.querySelector("main h1"),h1text=h1?h1.textContent:"",back=null;
  function apply(secs){
    var id=location.hash.slice(1),sel=secs[id]||null;
    [].forEach.call(box.children,function(c){c.classList.toggle("mcfiltered",!!sel&&c.id!==id);});
    var any=false;
    [].forEach.call(document.querySelectorAll("tr.pg"),function(tr){
      var a=tr.querySelector("a.ext"),show=!sel||!!(a&&sel.paths[norm(a.getAttribute("href").split("#")[0])]);
      tr.classList.toggle("mcfiltered",!show);
      var n=tr.nextElementSibling;if(n&&n.classList.contains("dev"))n.classList.toggle("mcfiltered",!show);
      if(show)any=true;
    });
    var head=document.querySelector(".devhead"),card=head&&head.nextElementSibling;
    [head,card].forEach(function(e){if(e)e.classList.toggle("mcfiltered",!!sel&&!any);});
    if(h1)h1.textContent=sel?sel.label:h1text;
    if(sel&&!back){back=el("a","mcall","Show every section");back.href="/admin/public/";if(h1&&h1.parentNode)h1.parentNode.insertBefore(back,h1.nextSibling);}
    if(back)back.hidden=!sel;
    [].forEach.call(document.querySelectorAll("#admin-nav a[data-mc]"),function(a){
      var h=a.getAttribute("href")||"";if(h.indexOf("/admin/public#")!==0)return;
      if(sel&&h==="/admin/public#"+id)a.setAttribute("aria-current","page");else a.removeAttribute("aria-current");
    });
  }
  fetch(src,{credentials:"include",cache:"no-store"}).then(function(r){return r.ok?r.json():null;}).then(function(d){
    if(!d||!Array.isArray(d.sections))return;
    var shown=0,secs={};
    d.sections.forEach(function(s){
      var sec=el("div","mcsec"),any=false;
      sec.id="sec-"+String(s.label).toLowerCase().replace(/[^a-z0-9]+/g,"-").replace(/^-+|-+$/g,""); /* the left nav links to it */
      sec.appendChild(el("h2",null,String(s.label)));
      var all=[].concat(s.pages||[]);(s.projects||[]).forEach(function(p){all=all.concat(p.pages||[]);});
      var paths={};all.forEach(function(p){var l=local(p.href);if(l)paths[norm(l.split("#")[0].split("?")[0])]=1;});
      secs[sec.id]={label:String(s.label),paths:paths};
      var top=grid(s.pages||[]);if(top){sec.appendChild(top);any=true;}
      (s.projects||[]).forEach(function(p){var g=grid(p.pages||[]);if(g){sec.appendChild(el("h3",null,String(p.name)));sec.appendChild(g);any=true;}});
      if(any){box.appendChild(sec);shown++;}
    });
    if(shown){box.hidden=false;apply(secs);window.addEventListener("hashchange",function(){apply(secs);});}
  }).catch(function(){});
})();
