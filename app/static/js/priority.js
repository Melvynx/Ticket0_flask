// todo : use font awrsomes
$(document).ready(() => {
  $("#new-comment-icon").on("click", () => {
    $("#new-comment-icon").hide();
    $("#new-comment").show();
  });
  $("#new-create").on("click", onCreate);
});

const onEditPriority = function (idPriority) {
  handleDisabled(idPriority, false);
  $(`#priority-edit-${idPriority}`).hide();
  $(`#priority-save-${idPriority}`).show();
  $(`#priority-save-${idPriority}`).show();
};

const onSavePriority = function (idPriority) {
  const name = $(`#priority-name-${idPriority}`).val();
  const level = $(`#priority-level-${idPriority}`).val();

  if (name.length <= 2 || name.length >= 50) {
    toggleSnackbar("Name need to be between 2 and 50 caracteres.", "danger");
    return;
  }

  if (isNaN(Number(level))) {
    toggleSnackbar("Level isn't a number.", "danger");
    return;
  }

  $(`#priority-edit-${idPriority}`).show();
  $(`#priority-save-${idPriority}`).hide();
  $(`#priority-save-${idPriority}`).hide();
  handleDisabled(idPriority, true);

  const newPriority = {
    priority: {
      name: name,
      description: $(`#priority-description-${idPriority}`).val(),
      level: Number(level),
    },
  };

  const newPriorityJson = JSON.stringify(newPriority);

  $.ajax({
    url: `${API_URL}/priorities/${idPriority}`,
    method: "PATCH",
    data: newPriorityJson,
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
