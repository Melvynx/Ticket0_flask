// on click button "edit" on the side of input name
const onEditName = function () {
  let name = $("#name");
  name.prop("disabled", false);
  $("#name-button-edit").hide();
  $("#name-button-save").show();
  name.focus();
};

autosize($("#description-category-new"));
autosize($("#description"));

// event focus out input name
const onSaveName = function (event) {
  // if save call by event
  if (event && event.key !== "Enter") return;

  let name = $("#name");

  if (name.val().length <= 2 || name.val().length >= 50) {
    toggleSnackbar("Name need to have between 2 and 50 caracters.", "danger");
    return;
  }

  name.prop("disabled", true);
  $("#name-button-edit").show();
  $("#name-button-save").hide();

  editCategory(API_CATEGORY_ID);
};

// on click button "edit" on the side of textarea description
const onEditDescription = function () {
  let description = $("#description");

  description.prop("disabled", false);
  $("#description-button-edit").hide();
  $("#description-button-save").show();
  description.focus();
};

// event focus out textarea description
const onSaveDescription = function (event) {
  // if save call by key event, do only if is enter key
  if (event && event.key !== "Enter") return;

  let description = $("#description");

  if (description.val().length < 5 || description.val().length >= 1000) {
    toggleSnackbar(
      "Description need to have between 5 and 1000 caracters.",
      "danger"
    );
    return;
  }
  description.prop("disabled", true);
  $("#description-button-edit").show();
  $("#description-button-save").hide();

  editCategory(API_CATEGORY_ID);
};

// idCategory: number, callback: Function
const editCategory = function (idCategory) {
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
      toggleSnackbar(state.status, state.state);
    },
    error: (result) => {
      console.warn(
        `Request status : ${result.status}, request state: ${result.responseJSON}`
      );
      toggleSnackbar("Database has problem. Try an other time.", "danger");
    },
  });
};

// items - edit (id for know what input need to be changed)
const onEditItem = function (id) {
  $("#item-name-" + id)
    .prop("disabled", false)
    .focus();
  $("#item-description-" + id).prop("disabled", false);
  $(`#item-edit-${id}`).hide();
  $(`#item-save-${id}`).show();
  $(`#item-delete-${id}`).show();
};

const onSaveItem = function (id) {
  const name = $("#item-name-" + id);
  name.prop("disabled", true);
  const description = $("#item-description-" + id);
  description.prop("disabled", true);

  if (name.val().length <= 2 || name.val().length >= 50) {
    toggleSnackbar("Name need to have between 2 and 50 caracters.", "danger");
    return;
  }
  if (description.val().length < 5 || description.val().length >= 1000) {
    toggleSnackbar(
      "Description need to have between 5 and 1000 caracters.",
      "danger"
    );
    return;
  }

  $(`#item-edit-${id}`).show();
  $(`#item-save-${id}`).hide();
  $(`#item-delete-${id}`).hide();
  updateItem(id);
};

// function to edit an item, API
const updateItem = function (idItem) {
  const name = $("#item-name-" + idItem).val();
  const description = $("#item-description-" + idItem).val();

  const newItem = { item: { name: name, description: description } };
  const newItemJson = JSON.stringify(newItem);

  $.ajax({
    url: `${API_URL}/items/${idItem}`,
    method: "PATCH",
    data: newItemJson,
    dataType: "json",
    contentType: "application/json",
    Accept: "application/json",
    success: (state) => {
      toggleSnackbar(state.status, state.state);
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

// function on toggle modal delete item

const toggleModalItem = function (itemID) {
  $("#validationDeleteModal").modal("show");
  $("#modal-delete-button").data("id", itemID);
  $("#modal-delete-button").data("link", "items");
  $("#modal-title-delete").text("Are you sure to delete this item ?");
  $("#modal-delete-body").html(
    generateModalText(
      "item",
      itemID,
      $(`#item-name-${itemID}`).val(),
      "all tickets that are linked will be deleted."
    )
  );
};

const toggleModalCategory = function (categoryID) {
  if (category_item.length > 6) {
    toggleSnackbar("I can't delete the category if there's an item left.", "danger");
    return;
  }
  $("#validationDeleteModal").modal("show");
  $("#modal-delete-button").data("id", categoryID);
  $("#modal-delete-button").data("link", "categories");
  $("#modal-title-delete").text("Are you sure to delete this category ?");
  $("#modal-delete-body").html(
    generateModalText(
      "category",
      categoryID,
      $(`#name`).val(),
      "all items linked with this category will be deleted too."
    )
  );
};

const onDelete = function () {
  id = $("#modal-delete-button").data("id");
  link = $("#modal-delete-button").data("link");

  $.ajax({
    url: `${API_URL}/${link}/${id}`,
    method: "DELETE",
    Accept: "application/json",
    success: (state) => {
      toggleSnackbar(state.status, state.state);
      window.location.reload();
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

const displayCreateBox = function () {
  $("#box-hide-item").hide();
};

// for categories.html
// function to try if champs is correct on create new category
const onSubmitCategory = function () {
  let title = $("#name-category-new").val();
  if (title.length < 2 || title.length > 100) {
    toggleSnackbar("Title need to have between 3 and 49 caractes.", "danger");
    return;
  }

  $("#form-categories").submit();
};
