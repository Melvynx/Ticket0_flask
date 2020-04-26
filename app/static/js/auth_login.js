$(document).ready(() => {
  $("#submit-form-login").on("click", onSubmit);
});

function onSubmit() {
  const username = $("#auth-username").val();
  const password = $("#auth-password").val();

  const login = { auth: { username: username, password: password } };

  $.ajax({
    url: `${API_URL}/login`,
    method: "POST",
    data: newTiqetJson,
    dataType: "json",
    contentType: "application/json",
    Accept: "application/json",
    success: (state) => {
      callback(state);
    },
    error: (result) => {
      console.warn("Request status :", result.status);
      toggleSnackbar("Database has problem. Try an other time.", "danger");
    },
  });
}
