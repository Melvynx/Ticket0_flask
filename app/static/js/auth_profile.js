$(document).ready(() => {
  $("#edit-button").on("click", onEdit);
  $("#save-button").on("click", onSave);
});

function onEdit() {
  $("#auth-lastname").prop("disabled", false);
  $("#auth-firstname").prop("disabled", false);
  $("#auth-email").prop("disabled", false);
  $("#edit-button").hide();
  $("#save-button").show();
}

function onSave() {
  const email = $("#auth-email").val();
  const emailHelper = checkEmail(email);
  if (!emailHelper.state) {
    toggleSnackbar(emailHelper.helper, "danger");
    return;
  }

  const newValues = {
    auth: {
      firstname: $("#auth-firstname").val(),
      lastname: $("#auth-lastname").val(),
      email: email,
    },
  };

  const newValuesJson = JSON.stringify(newValues);

  $.ajax({
    url: `${API_URL}/auth/${USER_ID}`,
    method: "PATCH",
    data: newValuesJson,
    dataType: "json",
    contentType: "application/json",
    Accept: "application/json",
    success: (state) => {
      toggleSnackbar(state.status, state.state);
      if (state.state === "success") {
        $("#auth-lastname").prop("disabled", true);
        $("#auth-firstname").prop("disabled", true);
        $("#auth-email").prop("disabled", true);
        $("#edit-button").show();
        $("#save-button").hide();
      }
    },
    error: (result) => {
      console.warn(
        `Request status : ${result.status}, request state:`,
        result.responseJSON
      );
      toggleSnackbar("Database has problem. Try an other time.", "danger");
    },
  });
}

function checkEmail(email) {
  const reggex = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  const isValidate = reggex.test(email);
  if (!isValidate) {
    return { helper: "Email is not a valid email.", state: false };
  }
  return { helper: "", state: true };
}
