$(document).ready(function() {
    //Preloader
    preloaderFadeOutTime = 500;
    function hidePreloader() {
        var preloader = $('.pre-loader');
        preloader.fadeOut(preloaderFadeOutTime);
    }
    hidePreloader();
});
