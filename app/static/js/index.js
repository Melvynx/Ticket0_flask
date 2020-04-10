const API_URL = "http://127.0.0.1:5000";

console.log("start");

// text: string, state: "danger" | "success"
function toggleSnackBar(text, state) {
  const snackBar = document.getElementById("snackbar");
  snackBar.innerHTML = text;
  setTimeout(() => snackBar.classList.remove("show"), 5000);
  console.log("state", state);
  switch (state) {
    case "danger":
      snackBar.classList.remove("sb-success");
      snackBar.classList.add("sb-danger");
      snackBar.classList.add("show");
      break;
    case "success":
      snackBar.classList.remove("sb-danger");
      snackBar.classList.add("sb-success");
      snackBar.classList.add("show");
      break;
    default:
      console.warn("toggleSnackBar(): state: 'danger' | 'success' != " + state);
      return;
  }
}

function editTiqet(idTiqet, values, callback) {
  const newTiqet = { tiqet: values };
  const newTiqetJson = JSON.stringify(newTiqet);
  console.log(newTiqet);

  fetch(`${API_URL}/tiqet/${idTiqet}`, {
    method: "PATCH",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: newTiqetJson,
  }).then((reponse) => {
    if (reponse.status !== 200) {
      console.warn("Tiqeto api has problem.");
      callback && callback({ state: "danger", status: "error server" });
      return;
    }

    reponse.json().then((state) => {
      callback && callback(state);
    });
  });
}
