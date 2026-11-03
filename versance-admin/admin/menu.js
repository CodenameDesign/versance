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
  var side=document.querySelector(".side");
  if(!side||!window.fetch)return;
  var root=document.documentElement,hostGated=/-mc\./.test(location.hostname),gated=hostGated;
  try{if(sessionStorage.getItem("mc-gated"))gated=true;}catch(e){}
  if(gated)root.classList.add("gating");
  var done=function(){root.classList.remove("gating");};
  setTimeout(done,3000); /* never leave the page blank if a request hangs */
  /* signed out on a gated host, the pages the gate would refuse are left out too (401), so a closed page is not offered */
  var signedOut=function(){try{sessionStorage.removeItem("mc-gated");}catch(e){}return gated?hideWhatIsRefused().then(done):done();};
  fetch("/admin/whoami.json",{credentials:"same-origin",cache:"no-store"}).then(function(r){return r.ok?r.json():null;}).then(function(d){
    if(!d||!d.email)return signedOut();
    try{sessionStorage.setItem("mc-gated","1");}catch(e){}
    var w=document.createElement("div");w.className="who";
    var e=document.createElement("div");e.className="who-email";e.textContent=d.email;e.title=d.email;
    var a=document.createElement("a");a.href="https://missioncontrol.futurebits.io/logout";a.textContent="Log out";
    w.appendChild(e);w.appendChild(a);side.appendChild(w);
    return hideWhatIsRefused().then(done);
  }).catch(signedOut);

  /* a link the person cannot open is not shown: each nav link, card and page row is asked for with a HEAD request, and the ones the gate refuses (403) are hidden */
  function hideWhatIsRefused(){
    var asked=[];
    function probe(href,hide){
      if(!href||href.charAt(0)!=="/")return Promise.resolve();
      var p=fetch(href,{method:"HEAD",credentials:"same-origin",cache:"no-store"}).then(function(r){if(r.status===403||r.status===401)hide();}).catch(function(){});
      asked.push(p);return p;
    }
    [].forEach.call(document.querySelectorAll(".side nav a:not(.navout)"),function(a){
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
