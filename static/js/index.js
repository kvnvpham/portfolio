let navbar = document.querySelector(".navbar");
let dropdown = document.querySelector(".bars");

dropdown.onclick = () => {
    navbar.classList.toggle("nav-active");
};

window.onscroll = () => {
    navbar.classList.remove("nav-active");
}

