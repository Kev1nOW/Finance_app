(function ($) {
  $(document).ready(function () {
    // Получаем селекторы для категории и подкатегории
    var $categorySelect = $('#id_category');
    var $subcategorySelect = $('#id_subcategory');
    var $typeSelect = $('#id_operations_type');

    // Обработчик изменения типа операции
    $typeSelect.on('change', function () {
      var typeId = $(this).val();
      if (typeId) {
        // Очищаем селектор категорий
        $categorySelect.empty().append('<option value="">---------</option>');
        $subcategorySelect
          .empty()
          .append('<option value="">---------</option>');

        // Получаем категории для выбранного типа
        $.getJSON(
          '/custom-admin/get_categories/',
          {
            operations_type: typeId,
          },
          function (data) {
            // Заполняем селектор категорий
            $.each(data, function (index, category) {
              $categorySelect.append(
                $('<option></option>').val(category.id).text(category.name)
              );
            });
          }
        );
      }
    });

    // Обработчик изменения категории
    $categorySelect.on('change', function () {
      var categoryId = $(this).val();
      $subcategorySelect.empty().append('<option value="">---------</option>');

      if (categoryId) {
        // Получаем подкатегории для выбранной категории
        $.getJSON(
          '/custom-admin/get_subcategories/',
          {
            category_id: categoryId,
          },
          function (data) {
            // Заполняем селектор подкатегорий
            $.each(data, function (index, item) {
              $subcategorySelect.append(
                $('<option></option>').val(item.id).text(item.name)
              );
            });

            // Если есть сохраненное значение подкатегории, выбираем его
            var savedSubcategoryId = $('#saved_subcategory_id').val();
            if (savedSubcategoryId) {
              $subcategorySelect.val(savedSubcategoryId);
            }
          }
        );
      }
    });

    // Если при загрузке страницы уже есть выбранная категория, загружаем подкатегории
    if ($categorySelect.val()) {
      // Сохраняем текущую подкатегорию
      var subcategoryId = $subcategorySelect.val();
      $('<input>')
        .attr({
          type: 'hidden',
          id: 'saved_subcategory_id',
          value: subcategoryId,
        })
        .appendTo('form');

      // Загружаем подкатегории
      $categorySelect.trigger('change');
    }
  });
})(django.jQuery);
