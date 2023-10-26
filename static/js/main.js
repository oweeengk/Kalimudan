document.querySelectorAll(".nav-item.dropdown").forEach(function (element) {
  // Mouseover event to show the dropdown menu
  element.addEventListener("mouseover", function () {
    element.querySelector(".dropdown-menu").classList.add("show")
    element.querySelector(".nav-link.dropdown-toggle").classList.add("active")
  })

  // Mouseout event to hide the dropdown menu
  element.addEventListener("mouseout", function () {
    if (
      !element
        .querySelector(".nav-link.dropdown-toggle")
        .classList.contains("pressed")
    ) {
      element.querySelector(".dropdown-menu").classList.remove("show")
      element
        .querySelector(".nav-link.dropdown-toggle")
        .classList.remove("active")
    }
  })

  // Handle click event on the dropdown link
  element
    .querySelector(".nav-link.dropdown-toggle")
    .addEventListener("click", function (e) {
      e.preventDefault() // Prevent the link from navigating immediately
      window.location.href = this.getAttribute("href") // Navigate to the specified URL
      this.classList.add("pressed")
    })
})
