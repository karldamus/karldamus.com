$( document ).ready(function() {
    $('#menu-open').on('click', function() {
        $('nav').addClass('open');
    });
    $('#menu-close').on('click', function() {
        $('nav').removeClass('open');
    });
});