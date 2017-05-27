$(function() {
   $('.tab-content').hide();
   $('#hidden_opt').hide();
   $(".nav-tabs a").click(function(){
        $(this).tab('show');
        $('.tab-content').show();
        $('#hidden_opt').show();
    });

    $('#hidden_opt').click(function() {
      $('.tab-content').hide();
      $(this).hide();
    })

$('#myCarousel .item').each(function(){
  var next = $(this).next();
  if (!next.length) {
    next = $(this).siblings(':first');
  }
  next.children(':first-child').clone().appendTo($(this));

  if (next.next().length>0) {
    next.next().children(':first-child').clone().appendTo($(this));
  }
  else {
    $(this).siblings(':first').children(':first-child').clone().appendTo($(this));
  }   
});

});