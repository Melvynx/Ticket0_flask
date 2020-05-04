const API_URL = "http://127.0.0.1:5000";

// text: string, state: "danger" | "success"
function toggleSnackbar(text, state) {
  const snackbar = $("#snackbar");
  snackbar.html(text);
  switch (state) {
    case "danger":
      snackbar.removeClass("sb-success");
      snackbar.addClass("sb-danger show");
      break;
    case "success":
      snackbar.removeClass("sb-danger");
      snackbar.addClass("sb-success show");
      break;
    default:
      console.warn("toggleSnackbar(): state: 'danger' | 'success' != " + state);
      return;
  }
  setTimeout(() => snackbar.removeClass("show"), 5000);
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
      callback && callback(state);
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

// by https://stackoverflow.com/a/21125098/12472736
function getCookie(name) {
  var match = document.cookie.match(new RegExp("(^| )" + name + "=([^;]+)"));
  if (match) return match[2];
}
