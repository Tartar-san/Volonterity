 $( function() {

      $('#multiselect').multiselect({

          buttonWidth: '100%',

          allSelectedText: 'Все',
          nonSelectedText: 'Оберіть інтереси',
      });
     $('.input-group .btn-default').css('background', '#c6f5d3').css('color', '#777');

     $('.input-group .btn-default .multiselect-selected-text').css('padding-left', '15%');



      $('.btn-default').css('text-align','center');
      $(".caret").hide();



      // $("#comment").autoGrow();

} );
