$(document).ready(() => {
  $("#submit-form-login").on("click", onSubmit);
});

function onSubmit() {
  const login = {
    auth: {
      username: $("#auth-username").val(),
      password: $("#auth-password").val(),
    },
  };
  const loginJson = JSON.stringify(login);

  $.ajax({
    url: `${API_URL}/login`,
    method: "POST",
    data: loginJson,
    dataType: "json",
    contentType: "application/json",
    Accept: "application/json",
    success: (state) => {
      toggleSnackbar(state.status, state.state);
    },
    error: (result) => {
      console.warn("Request status :", result.status);
      console.log(result.responseJSON);
      toggleSnackbar("Database has problem. Try an other time.", "danger");
    },
  });
}
