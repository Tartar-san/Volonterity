$(window).on("scroll", function() {

    if ($(window).scrollTop() <= 50) {
        //remove the background property so it comes transparent again (defined in your css)
        $(".navbar-fixed-top").removeClass("active");
        $(".navbar-fixed-top").css("background", "rgb(0,0,0,0.65)");


    } else {
        $(".navbar-fixed-top").addClass("active");
        $(".navbar-fixed-top").css("background", "rgb(0,0,0,0.50)"); //.....
        $(".panel-default").addClass("animated zoomIn");

    }


});
