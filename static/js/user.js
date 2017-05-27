 $( function() {
      var availableTags = [
        "Івано-Франківськ",
        "Київ",
        "Львів",
        "Нововолинськ",
        "Полтава",
        "Стрий",
        "Тернопіль",
        "Ужгород",
        "Червоноград",
        "Чернівці"
      ];


      $( ".ui-widget #tags" ).autocomplete({
        source: availableTags
      });
      $('#multiselect').multiselect({
          buttonWidth: '100%',
          allSelectedText: 'Все',
          nonSelectedText: 'Оберіть інтереси',
      });
      $('.btn-default').css('text-align','center');
      $(".caret").hide();

    } );