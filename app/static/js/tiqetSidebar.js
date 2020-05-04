$(document).ready(() => {
  $("#select-state").change(handleState);
  $("#select-category").change(handleCategory);
  $("#select-item").change(handleItem);
  $("#select-assigned").change(handleAssigned);
  $("#select-priority").change(handlePriority);

  handleCategory({ target: { value: $("#select-category").val() } });
});

const handleState = function (event) {
  const newState = checkNullValue(event.target.value);

  handleLoad(true);
  editTiqet(TIQET_ID, { fk_state: newState }, (state) => {
    handleLoad(false);
  });
};

const handleCategory = function (event) {
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
};

const handleAssigned = function (event) {
  const newAssigned = checkNullValue(event.target.value);

  handleLoad(true);
  editTiqet(TIQET_ID, { fk_assigned: newAssigned }, (state) => {
    handleLoad(false);
  });
};

const handlePriority = function (event) {
  const newPriority = checkNullValue(event.target.value);

  handleLoad(true);
  editTiqet(TIQET_ID, { fk_priority: newPriority }, (state) => {
    handleLoad(false);
    console.log(state);
  });
};

const handleItem = function (event) {
  const newItem = checkNullValue(event.target.value);

  handleLoad(true);
  editTiqet(TIQET_ID, { fk_item: newItem }, (state) => {
    handleLoad(false);
  });
};

const checkNullValue = function (value) {
  if (String(value).length === 0) {
    return null;
  }
  return value;
};

const showItems = function (idCategory, callback) {
  $.ajax({
    url: `${API_URL}/items/${idCategory}`,
    method: "GET",
    dataType: "json",
    Accept: "application/json",
    success: (items) => {
      callback && callback(items);
      pr;
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

const handleLoad = function (state) {
  if (state) {
    $("#spinner").show();
    $("#done-icon").hide();
    $("#spinner-load").show();
  } else {
    $("#spinner").hide();
    $("#done-icon").show();
    setTimeout(() => $("#spinner-load").hide(), 1000);
  }
};
