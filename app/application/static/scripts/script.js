// Menu
// document.querySelector("#home").addEventListener("mouseover", function(){
//   showText("#home-text")
// })
document.querySelector("#home").addEventListener("mouseout", function(){
  hiddenText("#home-text")
})
document.querySelector("#about").addEventListener("mouseover", function(){
  showText("#about-text")
})
document.querySelector("#about").addEventListener("mouseout", function(){
  hiddenText("#about-text")
})
document.querySelector("#portfolio").addEventListener("mouseover", function(){
  showText("#portfolio-text")
})
document.querySelector("#portfolio").addEventListener("mouseout", function(){
  hiddenText("#portfolio-text")
})
document.querySelector("#contact").addEventListener("mouseover", function(){
  showText("#contact-text")
})
document.querySelector("#contact").addEventListener("mouseout", function(){
  hiddenText("#contact-text")
})

function showText(selector) {
  const navItem = document.querySelector(selector).style.cssText = "display: inline;"
}
function hiddenText(selector) {
  const navItem = document.querySelector(selector).style.cssText = "display: none;"
}

  // Scroll to a certain element

document.getElementById("header-link").addEventListener("click", function(){
  goToInView("header")
})

document.getElementById("about-link").addEventListener("click", function(){
  goToInView("about-section")
})

document.getElementById("portfolio-link").addEventListener("click", function(){
  goToInView("portfolio-section")
})

document.getElementById("contact-link").addEventListener("click", function(){
  goToInView("contact-section")
})


function goToInView(selector) {
  const offsetTop = document.getElementById(selector).scrollIntoView({behavior: "smooth"});
}

  function goToContact() {    
    const offsetTop = document.querySelector("#contact-me").offsetTop;
    scroll({
      top: offsetTop,
      behavior: "smooth"
    });
  }

let sections = document.querySelectorAll("section")

let bulletHome = document.getElementById("bullet-home")
let bulletAbout = document.getElementById("bullet-about")
let bulletPortfolio = document.getElementById("bullet-portfolio")
let bulletContact = document.getElementById("bullet-contact")


window.addEventListener("scroll", function() {
  let fromTop = window.scrollY

  sections.forEach( link => {

    var section = document.getElementById(String(link.id))

    if (section.offsetTop <= fromTop && section.offsetTop + section.offsetHeight > fromTop){

      if (String(section.id).includes("home")) { 
        bulletHome.classList.add("current") 
      } else { 
        bulletHome.classList.remove("current") 
      }
      if (String(section.id).includes("about")) { 
        bulletAbout.classList.add("current") 
      } else { 
        bulletAbout.classList.remove("current") 
      }
      if (String(section.id).includes("portfolio")) { 
        bulletPortfolio.classList.add("current") 
      } else { 
        bulletPortfolio.classList.remove("current") 
      }
      if (String(section.id).includes("contact")) { 
        bulletContact.classList.add("current") 
      } else { 
        bulletContact.classList.remove("current") 
      }

    } 
  })
})