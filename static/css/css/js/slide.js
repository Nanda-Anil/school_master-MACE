$('.hero-slide').slick({
  dots: false,
  infinite: true,
  arrows:false,
  speed: 300,
  autoplay:true,
  slidesToShow: 1,
  slidesToScroll: 1,
  fade: true,
  cssEase: 'ease-in-out',
  responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1,
        infinite: true,
        dots: false
      }
    },
    {
      breakpoint: 600,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    }
    // You can unslick at a given breakpoint now by adding:
    // settings: "unslick"
    // instead of a settings object
  ]
});
$('#placed').owlCarousel({
    loop:true,
    margin:10,
    nav:true,
    dots:false,
    autoplay:true,
    autoplaySpeed: 3000,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        },
        1000:{
            items:5
        }
    }
})

$('#placed2').owlCarousel({
  loop:true,
  margin:10,
  nav:true,
  dots:false,
  autoplay:true,
  autoplay: true,
  autoplaySpeed: 3000,
  responsive:{
      0:{
          items:1
      },
      600:{
          items:3
      },
      1000:{
          items:5
      }
  }
})

// 

$('#tim').owlCarousel({
    loop:true,
    margin:10,
    nav:true,
    dots:false,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        },
        1000:{
            items:4
        }
    }
})

// SLICK
$('.slider-one').slick({
    dots: false,
    infinite: false,
    speed: 300,
    slidesToScroll: 1,
    slidesToShow: 1,
    asNavFor: '.slider-one-sub',
    arrows: false,
    infinite: true,
    cssEase: 'linear',
    focusOnSelect: true,
    

  });
  
 
  $('.slider-one-sub').slick({
    dots: false,
    // infinite: true,
    speed: 300,
    slidesToShow: ta,
    slidesToScroll: 1,
    autoplay:false,
    arrows: false,
    centerMode: true,
    infinite: true,
    asNavFor: '.slider-one',
    cssEase: 'linear',
    focusOnSelect: true,
  });

  $('.slider-two').slick({
    dots: false,
    infinite: true,
    speed: 300,
    slidesToScroll: 1,
    slidesToShow: 1,
    asNavFor: '.slider-two-sub',
    arrows: false,
    infinite: true,
    cssEase: 'linear',
    focusOnSelect: true,
    

  });



  $('.slider-two-sub').slick({
    dots: false,
    infinite: true,
    speed: 300,
    autoplay:false,
    slidesToShow: ra,
    slidesToScroll: 1,
    arrows: false,
    centerMode: true,
    infinite: true,
    asNavFor: '.slider-two',
    cssEase: 'linear',
    focusOnSelect: true,
  });

  $('.university').slick({
    dots: false,
    arrows: false,
    autoplay: false,
    infinite: true,
    speed: 300,
    slidesToShow: 8,
    slidesToScroll: 1,
    cssEase: 'linear',
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 8,
          slidesToScroll: 3,
          infinite: true,
          dots: false,
        }
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 8,
          slidesToScroll: 2,
          dots: false,
          arrows: false,
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 8,
          slidesToScroll: 1,
          dots: false,
          arrows: false,
        }
      }
    ]
  });