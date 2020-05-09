// todo : use font awrsomes
$(document).ready(() => {
  $("#new-comment-icon").on("click", () => {
    $("#new-comment-icon").hide();
    $("#new-comment").show();
  });
  $("#new-create").on("click", onCreate);
  $("#modal-delete-button").on("click", onDelete);
});

const onEditPriority = function (idPriority) {
  handleDisabled(idPriority, false);
  $(`#priority-edit-${idPriority}`).hide();
  $(`#priority-save-${idPriority}`).show();
  $(`#priority-save-${idPriority}`).show();
  $(`#priority-delete-${idPriority}`).show();
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
  $(`#priority-delete-${idPriority}`).hide();
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

const handleDisabled = function (id, state) {
  $(`#priority-name-${id}`).attr("disabled", state);
  $(`#priority-description-${id}`).attr("disabled", state);
  $(`#priority-level-${id}`).attr("disabled", state);
};

const onCreate = function () {
  const name = $("#new-name").val();
  const level = $("#new-level").val();

  if (name.length <= 2 || name.length >= 50) {
    toggleSnackbar("Name need to be between 2 and 50 caracteres.", "danger");
    return;
  }

  if (isNaN(Number(level))) {
    toggleSnackbar("Level isn't a number.", "danger");
    return;
  }

  const newPriority = {
    priority: {
      name: name,
      description: $("#new-description").val(),
      level: Number(level),
    },
  };

  const newPriorityJson = JSON.stringify(newPriority);

  $.ajax({
    url: `${API_URL}/priorities`,
    method: "POST",
    data: newPriorityJson,
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

const togglePriorityModal = function (id) {
  $("#validationDeleteModal").modal("show");
  $("#modal-delete-button").data("priorityid", id);
  $("#modal-delete-body").html(
    generateModalText(
      "priority",
      id,
      $(`#priority-name-${id}`).val(),
      "all tickets linked to this priority will no longer have it."
    )
  );
};

const onDelete = function (event) {
  const priorityId = $(event.target).data("priorityid");

  $.ajax({
    url: `${API_URL}/priorities/${priorityId}`,
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

const generateModalText = function (name, id, value, text) {
  const component = $(document.createElement("div"));
  const idBadge = $(document.createElement("p"));
  idBadge.text(`${name}'s id :${id}`);
  idBadge.addClass("badge badge-primary mr-4");
  const nameBadge = $(document.createElement("p"));
  nameBadge.text(`${name}'s name : ${value}`);
  nameBadge.addClass("badge badge-primary mr-4");
  const information = $(document.createElement("p"));
  information.text(`If you delete this ${name}, ${text}`);
  const irreversible = $(document.createElement("p"));
  irreversible.html("<b>This action is irreversible.</b>");
  component.append(idBadge);
  component.append(nameBadge);
  component.append(information);
  component.append(irreversible);

  return component;
};
