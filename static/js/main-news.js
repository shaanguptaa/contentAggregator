window.onload = function() {
    const preLoader = document.querySelector('.pre-loader');
    preLoader.style.opacity = 0;
    preLoader.addEventListener('transitionend', function() {
        preLoader.remove();
    });
    // document.querySelector('.pre-loader').remove();
};