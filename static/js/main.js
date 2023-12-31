function setActiveLink() {
  const currentURL = window.location.href
  const dropdownLinks = document.querySelectorAll(".nav-item.dropdown")

  dropdownLinks.forEach(function (element) {
    const dropdownLink = element.querySelector(".nav-link.dropdown-toggle")
    const linkURL = dropdownLink.getAttribute("href")

    if (currentURL === linkURL) {
      dropdownLink.classList.add("active")
    } else {
      dropdownLink.classList.remove("active")
    }
  })
}


document.querySelectorAll(".nav-item.dropdown").forEach(function (element) {
  const dropdownLink = element.querySelector(".nav-link.dropdown-toggle")
  const dropdownMenu = element.querySelector(".dropdown-menu")
  const menuItems = dropdownMenu.querySelectorAll(".dropdown-item")

  // Check if the number of menu items is more than 3
  if (menuItems.length > 3) {
    dropdownMenu.style.columnCount = 2;
  } else {
    dropdownMenu.style.columnCount = 1;
  }

  element.addEventListener("mouseover", function () {
    dropdownLink.classList.add("active")
    dropdownMenu.classList.add("show")
  })

  element.addEventListener("mouseout", function () {
    dropdownLink.classList.remove("active")
    dropdownMenu.classList.remove("show")
  })

  dropdownLink.addEventListener("click", function (e) {
    e.preventDefault()
    window.location.href = this.getAttribute("href")
    this.classList.add("pressed")
  })
})
/*
const startDateComputer = new Date("2019-08-06")
const startDateDressmaking = new Date("2022-09-27")
const startDateBreadAndPastry = new Date("2022-09-27")
const currentDate = new Date()

const timeDiffComputer = currentDate.getTime() - startDateComputer.getTime()
const daysAgoComputer = Math.floor(timeDiffComputer / (1000 * 3600 * 24))

const timeDiffDressmaking =
  currentDate.getTime() - startDateDressmaking.getTime()
const daysAgoDressmaking = Math.floor(timeDiffDressmaking / (1000 * 3600 * 24))

const timeDiffBreadAndPastry =
  currentDate.getTime() - startDateBreadAndPastry.getTime()
const daysAgoBreadAndPastry = Math.floor(
  timeDiffBreadAndPastry / (1000 * 3600 * 24)
)

document.getElementById(
  "computerDaysAgo"
).textContent = `${daysAgoComputer} days ago`
document.getElementById(
  "dressmakingDaysAgo"
).textContent = `${daysAgoDressmaking} days ago`
document.getElementById(
  "breadandpastryDaysAgo"
).textContent = `${daysAgoBreadAndPastry} days ago`
*/

window.addEventListener("load", function () {

  var loadingScreen = document.querySelector(".loading-screen")
  loadingScreen.style.opacity = 0

  setTimeout(function () {
    loadingScreen.style.display = "none"
  }, 0)
})
