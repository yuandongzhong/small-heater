$(function () {

  $(".js-create-category").click(function () {
    $.ajax({
      url: '/products/categories/create/',
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $('#modal-category').modal("show");
      },
      success: function (data) {
        $('#modal-category .modal-content').html(data.html_form);
      }
    });
  });

  $("#modal-category").on("submit", ".js-category-create-form", function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $('#category-list').html(data.html_category_list);
          $("#modal-category").modal("hide");
        } else {
          $("#modal-category .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  });

});