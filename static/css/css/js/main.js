
$('.mobile-toggle').click(function(){
    $('.res-nav').toggleClass('act');
});

$('li.has-sub i').click(function(){
  
  $(this).next().slideToggle("slow", "swing");
  if( $(this).hasClass('down')){
    $(this).removeClass('down');
    $(this).css('transform', "rotate(0)");
  }else{
    $(this).addClass('down');
    $(this).css('transform', "rotate(90deg)");
  }
})



// MOBILE TOGGLE

$('.mobile-toggle').click(function(){
  $('.mobile-toggle').toggleClass('open')
})

$(window).scroll(function()
{
 if ($(this).scrollTop() > 1)
 {
  $('.main-hd').addClass("stickhead");
  $('.res-nav').css('top',"75px")
 }
 else
 {
  $('.main-hd').removeClass("stickhead");
  $('.res-nav').css('top',"130px")
 }
});


// $('li.has-sub i').click(function()
// {
//   if( $('li.has-sub').hasClass('active')){
//     $('.res-nav').css('height', "100%")
//     $('.has-sub i').css('transform', "rotate(90deg)");
//   }
//   else{
//     $('.res-nav').css('height', "auto");
//     $('.has-sub i').css('transform', "rotate(0)");
//   }

// })

// ENQUIRY FORM
$('.enquiry-btn').click(function(){
    $('.enquiry-overlay').addClass('active');
    $('.enquiry-form').addClass('active');
});
$('.close-enquiry-form').click(function(){
    $('.enquiry-form').removeClass('active');
    $('.enquiry-overlay').removeClass('active');
})

//   TAB CURRIC

function openCity(evt, cityName) {
    // Declare all variables
    var i, tabcontent, tablinks;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
  }
  // Get the element with id="defaultOpen" and click on it



//


//STICKEY BUTTON MENU

$('.mainbtn').click(function(){
  $('.mainclosebtn').addClass('show');
  $('.main-em-lis').addClass('show');
})

$('.mainclosebtn').click(function(){
  $('.mainclosebtn').removeClass('show');
  $('.main-em-lis').removeClass('show');
});


// SEARCH BUTTON



// $('.search-blk').click(function(){
//   $('.search-input').toggleClass('open');
// });



//

function MatchHeight() {
  $('.test-cont')
    .matchHeight({})
  ;
}
