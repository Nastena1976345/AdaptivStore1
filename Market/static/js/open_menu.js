let openMenuBtn = document.getElementById('open-menu-btn');
let navBar = document.getElementById('nav-bar');

openMenuBtn.addEventListener('click', function (element) {

    let mavBarDisplay = getComputedStyle(navBar).display

    if (mavBarDisplay == 'none') {
        navBar.style.display = 'flex';
    }
    else if (mavBarDisplay == 'flex') {
        navBar.style.display = 'none';
    }
});