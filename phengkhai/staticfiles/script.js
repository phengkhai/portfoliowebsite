/*function openNav() {
    document.getElementById("mySidebar").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
  }*/
  
  /* Set the width of the sidebar to 0 and the left margin of the page content to 0 */
 /* function closeNav() {
    document.getElementById("mySidebar").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
  }*/
  function changeButton(x) {
    x.classList.toggle("change");
  }
  function togNav() {
    var nav = document.getElementById("mySidebar");
    if (nav.style.width == '250px') {
      nav.style.width = '0px';
      document.getElementById("main").style.marginLeft = "0";
    } else {
      nav.style.width = "250px";
      document.getElementById("main").style.marginLeft = "250px";
    }
  }