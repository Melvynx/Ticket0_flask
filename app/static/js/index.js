const API_URL = "http://127.0.0.1:5000";

// text: string, state: "danger" | "success"
function toggleSnackbar(text, state) {
  const snackbar = $("#snackbar");
  snackbar.html(text);
  setTimeout(() => snackbar.removeClass("show"), 5000);
  switch (state) {
    case "danger":
      snackbar.removeClass("sb-success");
      snackbar.addClass("sb-danger");
      snackbar.addClass("show");
      break;
    case "success":
      snackbar.removeClass("sb-danger");
      snackbar.addClass("sb-success");
      snackbar.addClass("show");
      break;
    default:
      console.warn("toggleSnackbar(): state: 'danger' | 'success' != " + state);
      return;
  }
}

function editTiqet(idTiqet, values, callback) {
  const newTiqet = { tiqet: values };
  const newTiqetJson = JSON.stringify(newTiqet);

  $.ajax({
    url: `${API_URL}/tiqet/${idTiqet}`,
    method: "PATCH",
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
