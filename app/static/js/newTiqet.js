$(document).ready(() => {
  categorySelectChange({ target: { value: $("#tiqet-category").val() } });
  $("select").niceSelect();
});

const categorySelectChange = function (event) {
  showItems(event.target.value, (items) => {
    $("#select-item").html(
      '<option value="null" selected data-display="- select item"> - </option>'
    );
    items.map((item) => {
      const option = $(document.createElement("option"));
      option.val(item.id_item);
      // niceSelect run script
      option.text(item.name.replace(/<|>/g, "|"));
      $("#select-item").append(option);
    });
    $("#select-item").niceSelect("update");
  });
};

const showItems = function (idCategory, callback) {
  $.ajax({
    url: `${API_URL}/items/${idCategory}`,
    method: "GET",
    dataType: "json",
    Accept: "application/json",
    success: (items) => {
      callback && callback(items);
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

const onCreate = function () {
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
};
