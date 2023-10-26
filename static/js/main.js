// Function to add the 'active' class to the appropriate link based on the current page
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

// Add 'active' class to the appropriate link on page load
setActiveLink()

// Mouseover event to show the dropdown menu on hover
document.querySelectorAll(".nav-item.dropdown").forEach(function (element) {
  const dropdownLink = element.querySelector(".nav-link.dropdown-toggle")
  const dropdownMenu = element.querySelector(".dropdown-menu")

  element.addEventListener("mouseover", function () {
    dropdownLink.classList.add("active")
    dropdownMenu.classList.add("show")
  })

  // Mouseout event to hide the dropdown menu on mouse away
  element.addEventListener("mouseout", function () {
    dropdownLink.classList.remove("active")
    dropdownMenu.classList.remove("show")
  })

  // Handle click event on the dropdown link
  dropdownLink.addEventListener("click", function (e) {
    e.preventDefault()
    window.location.href = this.getAttribute("href")
    this.classList.add("pressed")
  })
})
