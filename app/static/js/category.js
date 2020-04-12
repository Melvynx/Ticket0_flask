// on click button "edit" on the side of input name
function onEditName() {
  let name = $("#name");
  name.prop("disabled", false);
  $("#name-button-edit").hide();
  $("#name-button-save").show();
  name.focus();
}

// event focus out input name
function onSaveName(event) {
  // if save call by event
  if (event && event.key !== "Enter") return;

  let name = $("#name");

  if (name.val().length <= 2 || name.val().length >= 50) {
    toggleSnackBar("Name need to have between 2 and 50 caracters.", "danger");
    return;
  }

  name.prop("disabled", true);
  $("#name-button-edit").show();
  $("#name-button-save").hide();

  editCategory(API_CATEGORY_ID);
}

// on click button "edit" on the side of textarea description
function onEditDescription() {
  let description = $("#description");

  description.prop("disabled", false);
  $("#description-button-edit").hide();
  $("#description-button-save").show();
  description.focus();
}

// event focus out textarea description
function onSaveDescription(event) {
  // if save call by key event, do only if is enter key
  if (event && event.key !== "Enter") return;

  let description = $("#description");

  if (description.val().length < 5 || description.val().length >= 1000) {
    toggleSnackBar(
      "Description need to have between 5 and 1000 caracters.",
      "danger"
    );
    return;
  }
  description.prop("disabled", true);
  $("#description-button-edit").show();
  $("#description-button-save").hide();

  editCategory(API_CATEGORY_ID);
}

// idCategory: number, callback: Function
function editCategory(idCategory) {
  const description = $("#description").val();
  const name = $("#name").val();

  const newCategory = { category: { name: name, description: description } };
  const newCategoryJson = JSON.stringify(newCategory);

  $.ajax({
    url: `${API_URL}/categories/${idCategory}`,
    method: "PATCH",
    data: newCategoryJson,
    dataType: "json",
    contentType: "application/json",
    Accept: "application/json",
    success: (state) => {
      toggleSnackBar(state.status, state.state);
    },
    error: (result) => {
      console.warn(result.status);
      toggleSnackBar("Database has problem. Try an other time.", "danger");
    },
  });
}

// items - edit (id for know what input need to be changed)
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

// function to edit an item, API
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

// for categories.html
// function to try if champs is correct on create new category
function onSubmitCategory() {
  let title = document.getElementById("name-category-new").value;

  if (title.length < 2 || title.length > 50) {
    toggleSnackBar("Title need to have between 3 and 49 caractes.", "danger");
    return;
  }

  document.getElementById("form-categories").submit();
}
