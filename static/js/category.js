// name input
let nameFocus = false;

// on click button "edit" on the side of input name
function toggleEditName() {
  let inputName = document.getElementById("category-name");
  if (nameFocus) {
    return;
  }
  inputName.disabled = !inputName.disabled;
  document.getElementById("category-name-button").innerHTML = "Save";
  inputName.focus();
  nameFocus = true;
}

// event focus out input name
function onFocusOutName() {
  let inputName = document.getElementById("category-name");
  document.getElementById(
    "category-title"
  ).innerHTML = `Category : ${inputName.value}`;
  document.getElementById("category-name-button").innerHTML = "Edit";
  inputName.disabled = !inputName.disabled;
  setTimeout(() => (nameFocus = false), 100);

  editCategory(API_CATEGORY_ID, (state) => {
    toggleSnackBar(state.status, state.state);
  });
}

// description text-area
let descriptionFocus = false;

// on click button "edit" on the side of textarea description
function toggleEditDescription() {
  let inputDescription = document.getElementById("category-description");
  if (descriptionFocus) {
    return;
  }
  inputDescription.disabled = !inputDescription.disabled;
  document.getElementById("category-description-button").innerHTML = "Save";
  inputDescription.focus();
  descriptionFocus = true;
}

// event focus out textarea description
function onFocusOutDescription() {
  let inputDescription = document.getElementById("category-description");
  document.getElementById("category-description-button").innerHTML = "Edit";
  inputDescription.disabled = !inputDescription.disabled;
  setTimeout(() => (descriptionFocus = false), 100);

  editCategory(API_CATEGORY_ID, (state) => {
    toggleSnackBar(state.status, state.state);
  });
}

// idCategory: number, callback: Function
function editCategory(idCategory, callback) {
  const description = document.getElementById("category-description").value;
  const name = document.getElementById("category-name").value;

  const newCategory = { category: { name: name, description: description } };
  console.log("NEWCAT", newCategory);
  const newCategoryJson = JSON.stringify(newCategory);

  fetch(`${API_URL}/categories/${idCategory}`, {
    method: "PATCH",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: newCategoryJson,
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

// items - edit
function toggleEditItem(id) {
  let name = document.getElementById("item-name-" + id);
  let description = document.getElementById("item-description-" + id);
  let button = document.getElementById("item-button-" + id);

  if (name.disabled) {
    name.disabled = false;
    name.focus();
    description.disabled = false;
    button.innerHTML = "Save";
    button.classList.remove("btn-link");
    button.classList.add("btn-warning");
  } else {
    name.disabled = true;
    description.disabled = true;
    button.innerHTML = "Edit";
    button.classList.add("btn-link");
    button.classList.remove("btn-warning");
    editItem(name.value, description.value, id, (state) =>
      toggleSnackBar(state.status, state.state)
    );
  }
}

function editItem(name, description, idItem, callback) {
  const newItem = { item: { name: name, description: description } };
  const newItemJson = JSON.stringify(newItem);

  fetch(`${API_URL}/items/${idItem}`, {
    method: "PATCH",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: newItemJson,
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

function displayCreateBox() {
  document.getElementById("item-new-box").classList.add("hide");
}
