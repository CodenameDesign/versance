/* mobile menu: the dropdown arrow opens and closes the left nav */
document.addEventListener("click",function(e){
  var b=e.target.closest(".menubtn");
  if(b){var s=b.closest(".side"),o=s.classList.toggle("open");b.setAttribute("aria-expanded",String(o));b.setAttribute("aria-label",o?"Hide the admin menu":"Show the admin menu");return;}
  var s2=document.querySelector(".side.open");
  if(s2&&!e.target.closest(".side")){s2.classList.remove("open");var mb=s2.querySelector(".menubtn");mb.setAttribute("aria-expanded","false");mb.setAttribute("aria-label","Show the admin menu");}
});

/* who is signed in: on a host behind Mission Control's gate, /admin/whoami.json carries the person's email; elsewhere it is empty and nothing is added.
   On a gated host the links that are asked about stay invisible (class "gating") until the answers are in, so a link that is about to be hidden never flashes. */
(function(){
  var LAUNCHER="https://missioncontrol.futurebits.io/api/launcher/versance";
  var side=document.querySelector(".side");
  if(!side||!window.fetch)return;
  var root=document.documentElement,hostGated=/-mc\./.test(location.hostname),gated=hostGated;
  try{if(sessionStorage.getItem("mc-gated"))gated=true;}catch(e){}
  if(gated)root.classList.add("gating");
  /* the developer details are for people who are signed in: on a gated host they stay hidden until /admin/whoami.json names a person, and are not shown if it cannot be reached */
  if(hostGated)root.classList.add("nodev");
  var done=function(){root.classList.remove("gating");};
  setTimeout(done,3000); /* never leave the page blank if a request hangs */
  /* signed out on a gated host, the pages the gate would refuse are left out too (401), so a closed page is not offered */
  var signedOut=function(){try{sessionStorage.removeItem("mc-gated");}catch(e){}return gated?sectionsNav().then(hideWhatIsRefused).then(done):done();};
  fetch("/admin/whoami.json",{credentials:"same-origin",cache:"no-store"}).then(function(r){return r.ok?r.json():null;}).then(function(d){
    if(!d||!d.email)return signedOut();
    try{sessionStorage.setItem("mc-gated","1");}catch(e){}
    root.classList.remove("nodev");
    var w=document.createElement("div");w.className="who";
    var e=document.createElement("div");e.className="who-email";e.textContent=d.email;e.title=d.email;
    var a=document.createElement("a");a.href="https://missioncontrol.futurebits.io/logout";a.textContent="Log out";
    w.appendChild(e);w.appendChild(a);side.appendChild(w);
    return sectionsNav().then(hideWhatIsRefused).then(done);
  }).catch(signedOut);

  /* the left nav lists the account's sections, as set in Mission Control (Master Control > Pages), in place of the fixed links: a section made only of design-system
     pages goes to that guide, any other to its place on the Public page. It is Mission Control's own answer for the person (signed out, only the pages set to Anyone), so a section shows only with
     pages that person may open, and its number counts those. If the list cannot be loaded the fixed links stay. */
  function sectionsNav(){
    var nav=document.getElementById("admin-nav");
    if(!nav)return Promise.resolve();
    return fetch(LAUNCHER,{credentials:"include",cache:"no-store"}).then(function(r){return r.ok?r.json():null;}).then(function(d){
      if(!d||!Array.isArray(d.sections))return;
      var rows={};
      [].forEach.call(nav.querySelectorAll(".navrow"),function(r){var a=r.querySelector("a:not(.navout)");if(a)rows[a.getAttribute("href")]=r;});
      var here=location.pathname.replace(/[/]+$/,""),list=[];
      d.sections.forEach(function(s){
        var pages=[].concat(s.pages||[]);
        (s.projects||[]).forEach(function(p){pages=pages.concat(p.pages||[]);});
        if(!pages.length||typeof s.label!=="string")return;
        var guide,same=true;
        pages.forEach(function(p){
          var g=null;
          try{var m=/^[/]admin[/](system|identity)(?:[/]|$)/.exec(new URL(p.href,location.href).pathname);if(m)g="/admin/"+m[1];}catch(e){}
          if(guide===undefined)guide=g;else if(g!==guide)same=false;
        });
        if(!same)guide=null;
        var id="sec-"+s.label.toLowerCase().replace(/[^a-z0-9]+/g,"-").replace(/^-+|-+$/g,"");
        var target=guide||"/admin/public#"+id;
        var current=guide?(here===guide||here.indexOf(guide+"/")===0):(here==="/admin/public"&&location.hash==="#"+id);
        var row=guide&&rows[guide]?rows[guide].cloneNode(true):null,a;
        if(row){a=row.querySelector("a:not(.navout)");while(a.firstChild)a.removeChild(a.firstChild);}
        else{a=document.createElement("a");a.href=target;}
        a.setAttribute("data-mc","");
        if(current)a.setAttribute("aria-current","page");else a.removeAttribute("aria-current");
        var t=document.createElement("span");t.textContent=s.label;a.appendChild(t);
        var n=document.createElement("span");n.className="count";n.textContent=String(pages.length);a.appendChild(n);
        list.push(row||a);
      });
      if(!list.length)return;
      while(nav.firstChild)nav.removeChild(nav.firstChild);
      list.forEach(function(x){nav.appendChild(x);});
    }).catch(function(){});
  }

  /* a link the person cannot open is not shown: each nav link, card and page row is asked for with a HEAD request, and the ones the gate refuses (403) are hidden */
  function hideWhatIsRefused(){
    var asked=[];
    function probe(href,hide){
      if(!href||href.charAt(0)!=="/")return Promise.resolve();
      var p=fetch(href,{method:"HEAD",credentials:"same-origin",cache:"no-store"}).then(function(r){if(r.status===403||r.status===401)hide();}).catch(function(){});
      asked.push(p);return p;
    }
    [].forEach.call(document.querySelectorAll(".side nav a:not(.navout):not([data-mc])"),function(a){
      probe(a.getAttribute("href"),function(){(a.closest(".navrow")||a).hidden=true;});
    });
    [].forEach.call(document.querySelectorAll("tr.pg"),function(tr){
      var a=tr.querySelector("a.ext");
      if(a)probe(a.getAttribute("href"),function(){tr.hidden=true;if(tr.nextElementSibling&&tr.nextElementSibling.classList.contains("dev"))tr.nextElementSibling.hidden=true;});
    });
    /* the admin home: its cards, and a line of text that says only what is still there to open */
    var cards=[].slice.call(document.querySelectorAll(".tiles a.card"));
    if(cards.length)asked.push(Promise.all(cards.map(function(a){return probe(a.getAttribute("href"),function(){a.hidden=true;});})).then(function(){
      var shown=cards.filter(function(a){return !a.hidden;}).length,lead=document.querySelector("main .lead");
      if(shown===cards.length||!lead)return;
      lead.textContent=shown?"Developer tools for the Versance web app and browser-extension designs.":"There is nothing here for you to open yet. Ask the person who manages your account.";
    }));
    return Promise.all(asked);
  }
})();
