const navbar = document.querySelector(".navbar");
const dropdown = document.querySelector(".bars");

dropdown.onClick(() => {
    navbar.classList.toggle("nav-active");
})
