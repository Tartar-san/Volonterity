 $( function() {
      var availableTags = [
        "Івано-Франківськ",
        "Київ",
        "Львів",
        "Луцьк",
          "Рівне",
          "Одеса",
          "Вінниця",
          "Хмельницький",
          "Житомир",
          "Херсон",
          "Кропивницький",
          "Краматорськ",
          "Черкаси",
          "Дніпро",
          "Володимир-Волинський",
          "Кривий Ріг",
          "Луганськ",
          "Макіївка",
          "Чернігів",
          "Суми",
          "Борислав",
          "Броди",
          "Дебальцеве",
          "Добромиль",
          "Дрогобич",
          "Дубляни",
          "Жидачів",
          "Жмеринка",
          "Жовква",
          "Жовті Води",
          "Запоріжжя",
          "Заставна",
          "Збараж",
          "Здолбунів",
          "Золочів",
          "Ізюм",
          "Калуш",
          "Кам'янець-Подільський",
          "Канів",
          "Ковель",
          "Коломия",
          "Кременчук",
          "Лубни",
          "Лисичанськ",
          "Маріуполь",
          "Мелітополь",
          "Миколаїв",
          "Охтирка",
          "Ромни",
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
