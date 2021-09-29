const values = {"chess": 1, "film": 12, "basketputra": 1, "basketputri": 1, "band": 10, "dance": 7, "foto": 1, "debat": 3, "pidato": 1, "kosong": 1, "senjata": 1, "ganda": 2, "padus": 20, "design": 5};
// 11pm late-night javascript wkwk
var bosen;
function hideElement(id){
    document.getElementById(id).style.display = 'none'; // hide element
}

function showElement(id){
    document.getElementById(id).style.display = ''; // i prefer '' instead of 'block'
}

function cslOptions(lomba){
    for(let i=1; i<=values[lomba]; i++) {
        showElement("section-nama"+i.toString());
        showElement("section-telepon"+i.toString());
        showElement("section-email"+i.toString());
        showElement("section-lahir"+i.toString());
    }

    for(let i=values[lomba]+1; i<=20; i++) {
        hideElement("section-nama"+i.toString());
        hideElement("section-telepon"+i.toString());
        hideElement("section-email"+i.toString());
        hideElement("section-lahir"+i.toString());
    }

    for(let i=1; i<=values[lomba]; i++) {
        document.getElementById("nama"+i.toString()).setAttribute("required","");
        document.getElementById("telpon"+i.toString()).setAttribute("required","");
        document.getElementById("email"+i.toString()).setAttribute("required","");
        document.getElementById("lahir"+i.toString()).setAttribute("required","");
    }

    for(let i=values[lomba]+1; i<=20; i++) {
        document.getElementById("nama"+i.toString()).removeAttribute("required");
        document.getElementById("telpon"+i.toString()).removeAttribute("required");
        document.getElementById("email"+i.toString()).removeAttribute("required");
        document.getElementById("lahir"+i.toString()).removeAttribute("required");
    }
}
var countDownDate = new Date("Oct 11, 2021 16:00:00").getTime();
  var x = setInterval(function() {
    var now = new Date().getTime();
    var distance = countDownDate - now;
    var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);
    document.getElementById("D").innerHTML = (days<10)? "0" + days : days;
    document.getElementById("H").innerHTML = (hours<10)? "0" + hours : hours;
    document.getElementById("M").innerHTML = (minutes<10)? "0" + minutes : minutes;
    document.getElementById("S").innerHTML = (seconds<10)? "0" + seconds : seconds;
    if (distance < 0) {
      clearInterval(x);
      document.getElementById("Title").innerHTML = "CSL Day "+ Math.abs(days);
      document.getElementById("Div-Timer").style.display = "none";
      document.getElementById("Coming-Soon").style.display = "none";
      document.getElementById("Title").style.display = "block";
    }
  }, 0);

const toggleButton = document.getElementsByClassName('toggle-button')[0]
const navbarLinks = document.getElementsByClassName('navbar-links')[0]

toggleButton.addEventListener('click', () => {
  navbarLinks.classList.toggle('active')
})

var slideIndex = 0;
showSlides();

function showSlides() {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}
  slides[slideIndex-1].style.display = "block";
  setTimeout(showSlides, 10000); // Change image every 5 seconds
}