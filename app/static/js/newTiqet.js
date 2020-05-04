$(document).ready(() => {
  categorySelectChange({ target: { value: $("#tiqet-category").val() } });
  $("select").niceSelect();
});

function categorySelectChange(event) {
  showItems(event.target.value, (items) => {
    $("#select-item").html(
      '<option value="null" selected data-display="- select item"> - </option>'
    );
    items.map((item) => {
      $("#select-item").append(
        `<option value="${item.id_item}">${item.name}</option>`
      );
    });
    $("#select-item").niceSelect("update");
  });
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

function onCreate() {
  title = $("#tiqet-title").val();
  item = $("#select-item").val();

  if (title.length < 2 || title.length > 51) {
    toggleSnackbar("Title need to have between 3 and 50 caracteres", "danger");
    return;
  }

  if (item === "null") {
    toggleSnackbar("Need to have 1 selected item.", "danger");
    return;
  }

  $("#tiqet-form-new").submit();
}
