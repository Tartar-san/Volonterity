$(window).on("scroll", function() {

    if($(window).scrollTop() > 50) {
        $(".navbar-fixed-top").addClass("active");
        $(".navbar-fixed-top").css("background", "rgb(0,0,0,0.50)");

    }


    else {
        //remove the background property so it comes transparent again (defined in your css)
       $(".navbar-fixed-top").removeClass("active");
       $(".navbar-fixed-top").css("background", "rgb(0,0,0,0.65)");


    }

    $(".panel").addClass("animated zoomIn");

});/**
 * Created by yaryna on 13.06.17.
 */
