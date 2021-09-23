window.onscroll = function() {
    scroll()
};

function scroll() {
    if (document.body.scrollTop > 20 ||
            document.documentElement.scrollTop > 20) {
        document.getElementById("navlist").style.top = "0";
    }
    else {
        document.getElementById("navlist").style.top
                = "-60px";
    }
}

const hamburger = document.querySelector(".ham");  
 const navsub = document.querySelector(".nav-sub");  
 hamburger.addEventListener('click', () => {  
  hamburger.classList.toggle("change")  
  navsub.classList.toggle("nav-change")  
 });  