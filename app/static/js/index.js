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
      snackBar.classList.add("sb-danger");
      snackBar.classList.add("show");
      break;
    case "success":
      snackBar.classList.add("sb-success");
      snackBar.classList.add("show");
      break;
    default:
      console.warn("toggleSnackBar(): state: 'danger' | 'success' != " + state);
      return;
  }
}
