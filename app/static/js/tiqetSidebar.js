$(document).ready(() => {
  $("#select-state").change(handleState);
  $("#select-category").change(handleCategory);
  $("#select-item").change(handleItem);
  $("#select-assigned").change(handleAssigned);
  $("#select-priority").change(handlePriority);

  handleCategory({ target: { value: $("#select-category").val() } });
});

function handleState(event) {
  const newState = checkNullValue(event.target.value);

  handleLoad(true);
  editTiqet(TIQET_ID, { fk_state: newState }, (state) => {
    handleLoad(false);
  });
}

function handleCategory(event) {
  handleLoad(true);
  showItems(event.target.value, (items) => {
    handleLoad(false);
    $("#select-item").html(
      '<option value="null" selected data-display="- select item"> - </option>'
    );
    items.map((item) => {
      $("#select-item").append(
        `<option value="${item.id_item}" ${
          ITEM_ID === String(item.id_item) ? "selected" : ""
        }>${item.name}</option>`
      );
    });
    $("#select-item").niceSelect("update");
  });
}

function handleAssigned(event) {
  const newAssigned = checkNullValue(event.target.value);

  handleLoad(true);
  editTiqet(TIQET_ID, { fk_assigned: newAssigned }, (state) => {
    handleLoad(false);
  });
}

function handlePriority(event) {
  const newPriority = checkNullValue(event.target.value);

  handleLoad(true);
  editTiqet(TIQET_ID, { fk_priority: newPriority }, (state) => {
    handleLoad(false);
    console.log(state);
  });
}

function handleItem(event) {
  const newItem = checkNullValue(event.target.value);

  handleLoad(true);
  editTiqet(TIQET_ID, { fk_item: newItem }, (state) => {
    handleLoad(false);
  });
}

function checkNullValue(value) {
  if (String(value).length === 0) {
    return null;
  }
  return value;
}

function showItems(idCategory, callback) {
  $.ajax({
    url: `${API_URL}/items/${idCategory}`,
    method: "GET",
    dataType: "json",
    Accept: "application/json",
    success: (items) => {
      callback && callback(items);
    },
    error: (result) => {
      console.warn("Request status :", result.status);
      toggleSnackbar("Database has problem. Try an other time.", "danger");
    },
  });
}

function handleLoad(state) {
  if (state) {
    $("#spinner").show();
    $("#done-icon").hide();
    $("#spinner-load").show();
  } else {
    $("#spinner").hide();
    $("#done-icon").show();
    setTimeout(() => $("#spinner-load").hide(), 1000);
  }
}
