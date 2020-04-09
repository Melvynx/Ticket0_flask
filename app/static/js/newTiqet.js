function categorySelectChange(event) {
  getItemByCategory(event.target.value, (items) => {
    setSelectItem(items);
  });
}

function setSelectItem(items) {
  let HTMLOptions = `<option value="null" selected> - </option>`;
  items.map((item) => {
    HTMLOptions += "\n";
    HTMLOptions += `<option value="${item.id_item}">${item.name}</option>`;
  });
  document.getElementById("select-item").innerHTML = HTMLOptions;
}

function getItemByCategory(idCategory, callback) {
  fetch(`${API_URL}/items/${idCategory}`, {
    method: "GET",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
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

function onCreate() {
  title = document.getElementById("tiqet-title");
  item = document.getElementById("select-item");
  submitButton = document.getElementById("submit-form");

  if (title.value.length < 2 || title.value.length > 51) {
    toggleSnackBar("Title need to have between 3 and 50 caracteres", "danger");
    return;
  }

  if (item.value === "null") {
    toggleSnackBar("Need to have 1 selected item.", "danger");
    return;
  }

  document.getElementById("tiqet-form-new").submit();
}
