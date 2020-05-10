const API_URL = "http://127.0.0.1:5000";

// text: string, state: "danger" | "success"
const toggleSnackbar = function (text, state) {
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
};

const editTiqet = function (idTiqet, values, callback) {
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
};

// by https://stackoverflow.com/a/21125098/12472736
const getCookie = function (name) {
  var match = document.cookie.match(new RegExp("(^| )" + name + "=([^;]+)"));
  if (match) return match[2];
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
