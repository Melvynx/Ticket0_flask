// todo : use font awrsomes
$(document).ready(() => {
  $("#modal-delete-button").on("click", onDelete);
});

const onEditName = function (idState) {
  $(`#name-${idState}`).hide();
  $(`#name-i-${idState}`).show();
};

const onSaveName = function (idState) {
  $(`#name-${idState}`)
    .show()
    .text($(`#name-i-${idState}`).val());
  const name = $(`#name-i-${idState}`).hide().val();
  const checked = $(`#display-${idState}`).prop("checked");

  const newState = { state: { name: name, display: checked } };

  const newStateJson = JSON.stringify(newState);

  $.ajax({
    url: `${API_URL}/states/${idState}`,
    method: "PATCH",
    data: newStateJson,
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

const onEditDisplay = function (idState) {
  const name = $(`#name-i-${idState}`).val();
  const checked = $(`#display-${idState}`).prop("checked");
  const newState = { state: { name: name, display: checked } };

  const newStateJson = JSON.stringify(newState);

  $.ajax({
    url: `${API_URL}/states/${idState}`,
    method: "PATCH",
    data: newStateJson,
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

const onCreate = function () {
  const name = $(`#new-name`).val();

  const newState = { state: { name: name } };

  const newStateJson = JSON.stringify(newState);

  $.ajax({
    url: `${API_URL}/states`,
    method: "POST",
    data: newStateJson,
    dataType: "json",
    contentType: "application/json",
    Accept: "application/json",
    success: (state) => {
      toggleSnackbar(state.status, state.state);
      document.location.reload();
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

const toggleDelete = function (id) {
  $("#validationDeleteModal").modal("show");
  $("#modal-delete-button").data("stateid", id);
  $("#modal-delete-body").html(
    generateModalText(
      "state",
      id,
      $(`#name-i-${id}`).val(),
      "Beware, all tickets linked to this state will be definitively deleted too."
    )
  );
};

const onDelete = function (event) {
  const stateId = $(event.target).data("stateid");

  $.ajax({
    url: `${API_URL}/states/${stateId}`,
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
