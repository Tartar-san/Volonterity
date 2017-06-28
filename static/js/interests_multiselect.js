 $( function() {

      $('#multiselect').multiselect({

          buttonWidth: '100%',

          allSelectedText: 'Все',
          nonSelectedText: 'Оберіть інтереси',
      });
     $('.input-group .btn-default').css('background', '#rgba(130, 200, 90, 0.8)').css('color', '#555');

     $('.input-group .btn-default .multiselect-selected-text').css('padding-left', '15%');



      $('.btn-default').css('text-align','center');
      $(".caret").hide();

} );
