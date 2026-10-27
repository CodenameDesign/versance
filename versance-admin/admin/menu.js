/* mobile menu: the dropdown arrow opens and closes the left nav */
document.addEventListener("click",function(e){
  var b=e.target.closest(".menubtn");
  if(b){var s=b.closest(".side"),o=s.classList.toggle("open");b.setAttribute("aria-expanded",String(o));b.setAttribute("aria-label",o?"Hide the admin menu":"Show the admin menu");return;}
  var s2=document.querySelector(".side.open");
  if(s2&&!e.target.closest(".side")){s2.classList.remove("open");var mb=s2.querySelector(".menubtn");mb.setAttribute("aria-expanded","false");mb.setAttribute("aria-label","Show the admin menu");}
});
