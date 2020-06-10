// todo : use font awrsomes
$(document).ready(() => {
  $("#new-comment-icon").on("click", () => {
    $("#new-comment-icon").hide();
    $("#new-comment").show();
  });
  $("#new-create").on("click", onCreate);
  $("#modal-delete-button").on("click", onDelete);
});

const onEditLabel = function (idLabel) {
  handleDisabled(idLabel, false);
  $(`#label-edit-${idLabel}`).hide();
  $(`#label-save-${idLabel}`).show();
  $(`#label-save-${idLabel}`).show();
  $(`#label-delete-${idLabel}`).show();
};

const onSaveLabel = function (idLabel) {
  const name = $(`#label-name-${idLabel}`).val();
  const color = $(`#label-color-${idLabel}`).val();

  if (name.length <= 2 || name.length >= 50) {
    toggleSnackbar("Name need to be between 2 and 50 caracteres.", "danger");
    return;
  }

  if (isNaN(Number(color))) {
    toggleSnackbar("Level isn't a number.", "danger");
    return;
  }

  $(`#label-edit-${idLabel}`).show();
  $(`#label-save-${idLabel}`).hide();
  $(`#label-delete-${idLabel}`).hide();
  $(`#label-save-${idLabel}`).hide();
  handleDisabled(idLabel, true);

  const newLabel = {
    label: {
      name: name,
      description: $(`#label-description-${idLabel}`).val(),
      color: Number(color),
    },
  };

  const newLabelJson = JSON.stringify(newLabel);

  $.ajax({
    url: `${API_URL}/priorities/${idLabel}`,
    method: "PATCH",
    data: newLabelJson,
    dataType: "json",
    contentType: "application/json",
    Accept: "application/json",
    success: (state) => {
      toggleSnackbar(state.status, state.state);
    },
    error: (result) => {
      console.warn(
        `Request status : ${result.status}, request state:`,
        result.responseJSON
      );
      toggleSnackbar("Database has problem. Try an other time.", "danger");
    },
  });
};

const handleDisabled = function (id, state) {
  $(`#label-name-${id}`).attr("disabled", state);
  $(`#label-description-${id}`).attr("disabled", state);
  $(`#label-color-${id}`).attr("disabled", state);
};

const onCreate = function () {
  const name = $("#new-name").val();
  const color = $("#new-color").val();

  if (name.length <= 2 || name.length >= 50) {
    toggleSnackbar("Name need to be between 2 and 50 caracteres.", "danger");
    return;
  }

  if (isNaN(Number(color))) {
    toggleSnackbar("Level isn't a number.", "danger");
    return;
  }

  const newLabel = {
    label: {
      name: name,
      description: $("#new-description").val(),
      color: Number(color),
    },
  };

  const newLabelJson = JSON.stringify(newLabel);

  $.ajax({
    url: `${API_URL}/priorities`,
    method: "POST",
    data: newLabelJson,
    dataType: "json",
    contentType: "application/json",
    Accept: "application/json",
    success: (state) => {
      toggleSnackbar(state.status, state.state);
      window.location.reload();
    },
    error: (result) => {
      console.warn(
        `Request status : ${result.status}, request state:`,
        result.responseJSON
      );
      toggleSnackbar("Database has problem. Try an other time.", "danger");
    },
  });
};

const toggleLabelModal = function (id) {
  $("#validationDeleteModal").modal("show");
  $("#modal-delete-button").data("labelid", id);
  $("#modal-delete-body").html(
    generateModalText(
      "label",
      id,
      $(`#label-name-${id}`).val(),
      "all tickets linked to this label will no longer have it."
    )
  );
};

const onDelete = function (event) {
  const labelId = $(event.target).data("labelid");

  $.ajax({
    url: `${API_URL}/priorities/${labelId}`,
    method: "DELETE",
    Accept: "application/json",
    success: (state) => {
      toggleSnackbar(state.status, state.state);
      window.location.reload();
    },
    error: (result) => {
      console.warn(
        `Request status : ${result.status}, request state:`,
        result.responseJSON
      );
      toggleSnackbar("Database has problem. Try an other time.", "danger");
    },
  });
};
