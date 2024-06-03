$(document).ready(function () {
  /********************************************** Navigation ********************************************/

  //closes responsive menu when a scroll trigger link is clicked
  $(".nav-link").click(function () {
    $(".navbar-collapse").collapse("hide");
  });

  //
  $("body").scrollspy({
    target: "#mainNav",
    offset: 70,
  });

  //On scroll down if offset is higher than 50 pixels add navBar shrink else remove that class
  $(window).scroll(function () {
    if ($("#mainNav").offset().top > 50) {
      $("#mainNav").addClass("navbar-shrink");
    } else {
      $("#mainNav").removeClass("navbar-shrink");
    }
  });

  //
  $(window).scroll(function () {
    if ($("#mainNav").offset().top > 1000) {
      $("#mainNav").addClass("navbar-color");
    } else {
      $("#mainNav").removeClass("navbar-color");
    }
  });
});
