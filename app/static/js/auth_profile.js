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
  $("#auth-lastname").prop("disabled", true).val();
  $("#auth-firstname").prop("disabled", true).val();
  const email = $("#auth-email").prop("disabled", true).val();

  const emailHelper = checkEmail(email);

  if (!emailHelper.state) {
    toggleSnackbar(emailHelper.helper, "danger");
    return;
  }

  $.ajax({
    url: `${API_URL}/auth/${USER_ID}`,
    method: "POST",
    data: credentialJson,
    dataType: "json",
    contentType: "application/json",
    Accept: "application/json",
    success: (state) => {
      resolve(state);
    },
    error: (result) => {
      resolve(false);
      console.warn(result.responseJSON);
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
