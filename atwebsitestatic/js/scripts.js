$(function () {
    $(document).scroll(function () {
      var $nav = $("#main-nav");
      $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
    });
  });


$(function() {
    $(document).ready(function() {
        $('.owl-carousel').owlCarousel({
            items:1,
            loop:true,
            margin:10,
            autoplay:true,
            animateOut: 'slideOutLeft',
            animateIn: 'slideInRight',
            autoplayTimeout:5000,
            autoplayHoverPause:true,
            center: true,
        });
    });
});