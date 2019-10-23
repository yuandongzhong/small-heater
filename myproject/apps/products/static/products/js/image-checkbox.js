$(function () {


  // image gallery

  // init the state from the input
  $(".image-checkbox").each(function () {
    if ($(this).find('input[type="checkbox"]').first().attr("checked")) {
      $(this).addClass('image-checkbox-checked');
    } else {
      $(this).removeClass('image-checkbox-checked');
    }
  });

  // sync the state to the input
  $(".image-checkbox").on("click", function (e) {
    $(this).toggleClass('image-checkbox-checked');
    var $checkbox = $(this).find('input[type="checkbox"]');
    $checkbox.prop("checked", !$checkbox.prop("checked"))

    e.preventDefault();
  });


  // Get photo id from selected checkboxes
  getPhotoList = function () {
    var photos = [];
    $.each($("input[type='checkbox']:checked"), function () {
      photos.push($(this).val());
    });
    return photos
  }


  // Delete photos
  $("#photo-container").on("click", ".js-delete-photo", function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $('#modal-photo').modal("show");
      },
      success: function (data) {
        $('modal-photo, .modal-content').html(data.html_form);
      }
    });
  });


  $("#modal-photo").on("submit", ".js-photo-delete-form", function () {
    var form = $(this);
    var csrfmiddlewaretoken = document.getElementsByName('csrfmiddlewaretoken')[0].value
    $.ajax({
      url: form.attr("action"),
      // data: form.serialize(),
      data: {
        'photos[]': getPhotoList(),
        'csrfmiddlewaretoken': csrfmiddlewaretoken
      },
      type: form.attr("method"),
      dataType: 'json',
      beforeSend: function () {},
      success: function (data) {
        if (data.success) {
          $("#photo-list").html(data.html_photo_list);
          $("#modal-photo").modal("hide");
        }
      }
    });
    return false;
  });
});