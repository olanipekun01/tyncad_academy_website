$(function () {
    $(document).scroll(function () {
      var $nav = $("#main-nav");
      $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
    });
  });


$(function() {
    // $(document).ready(function() {
        var owl = $('.owl-carousel').owlCarousel({
            items:1,
            loop:true,
            margin:10,
            autoplay:true,
            animateOut: 'animate__slideOutLeft',
            animateIn: 'animate__slideInRight',
            autoplayTimeout:5000,
            autoplayHoverPause:true,
            center: true,
        });
    // });

    $('.customNextBtn').click(function() {
        console.log('got here');
        owl.trigger('next.owl.carousel');
    })
    // Go to the previous item
    $('.customPrevBtn').click(function() {
        owl.trigger('prev.owl.carousel');
    })
    
});