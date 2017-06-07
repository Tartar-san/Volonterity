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
});
