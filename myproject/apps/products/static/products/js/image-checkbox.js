$(function () {

  var selectionCount = function () {
    return $.find('input[type="checkbox"]:checked').length
  }

  // init the check state from the input
  $(".image-checkbox").each(function () {
    if ($(this).find('input[type="checkbox"]').first().attr("checked")) {
      $(this).addClass('image-checkbox-checked');
    } else {
      $(this).removeClass('image-checkbox-checked');
    }
  });


  var activateCheckbox = function () {
    // sync the check state to the input
    $(".image-checkbox").on("click", function (e) {
      $(this).toggleClass('image-checkbox-checked');
      var $checkbox = $(this).find('input[type="checkbox"]');
      $checkbox.prop("checked", !$checkbox.prop("checked"))

      if (selectionCount() > 0) {
        // activate delete button
        $('button.js-delete-photo').prop('disabled', false);
      } else {
        // disable delete button
        $('button.js-delete-photo').prop('disabled', true);
      }
      e.preventDefault();
    });
  }

  // Edit button
  $(".js-edit-photo").on("click", function (e) {
    var editButton = $(this);
    editButton.hide();
    $(".delete-button-group").show();
    $(".image-checkbox").each(function () {
      $(this).find('input[type="checkbox"]').first().prop('disabled', false);
    });
    activateCheckbox();
    $("button.js-upload-photos").hide();
  });

  // cancel button
  $(".js-delete-photo-cancel").on("click", function (e) {
    cancelDeletion();
  });

  var cancelDeletion = function () {
    $(".delete-button-group").hide();
    $(".js-edit-photo").show();
    $('button.js-delete-photo').prop('disabled', true);
    // Remove click listener from clickbox
    $(".image-checkbox").off('click');
    $("button.js-upload-photos").show();
    $(".image-checkbox").each(function () {
      $(this).find('input[type="checkbox"]').first().prop('disabled', true);
      $(this).removeClass('image-checkbox-checked');
      var $checkbox = $(this).find('input[type="checkbox"]');
      $checkbox.prop("checked", false)
    });
  }

  // Get photo id from selected checkboxes
  var getPhotoList = function () {
    var photos = [];
    $.each($("input[type='checkbox']:checked"), function () {
      photos.push($(this).val());
    });
    return photos;
  }

  // Activate photo deletion confirmation
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
        $('#modal-photo').find('.modal-content').first().html(data.html_form);
      }
    });
  });


  // Confirm the deletion
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
          cancelDeletion();
        }
      }
    });
    return false;
  });
});