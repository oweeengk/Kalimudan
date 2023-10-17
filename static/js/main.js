// Add event listener for dropdown menu items
document.querySelectorAll(".nav-item.dropdown").forEach(function (element) {
  element.addEventListener("mouseover", function () {
    element.querySelector(".dropdown-menu").classList.add("show")
  })

  element.addEventListener("mouseout", function () {
    element.querySelector(".dropdown-menu").classList.remove("show")
  })

  // Handle click event on the dropdown link
  element
    .querySelector(".nav-link.dropdown-toggle")
    .addEventListener("click", function (e) {
      e.preventDefault() // Prevent the link from navigating immediately
      window.location.href = this.getAttribute("href") // Navigate to the specified URL
    })
})
