$(document).ready(() => {
  $("#submit-form-login").on("click", onSubmit);
});

function onSubmit() {
  console.log("jimmy");
  $("#auth-form-login").submit();
}
