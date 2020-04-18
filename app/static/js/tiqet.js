$(document).ready(() => {
  $("#content").html($("#content").html().replace(/\r?\n/g, "<br>"));
});

autosize($("#input-content"));

/* title script "title.html" */
function toggleEditTitle() {
  $("#title").hide();
  $("#image-title").hide();
  $("#input-title").show().val($("#title").html()).on("keyup", titleSave).focus();
  $("#button-title").show();
}

function titleSave(event) {
  if (event) if (event.key !== "Enter") return;
  const input = $("#input-title");

  if (input.val().length < 3 || input.val().length > 50) {
    toggleSnackbar("Title need to have between 4 and 49 caractes.", "danger");
  } else {
    $("#image-title").show();
    input.hide();
    $("#title").html(input.val()).show();
    $("#button-title").hide();
    editTiqet(TIQET_ID, { title: input.val() }, (state) => {
      toggleSnackbar(state.status, state.state);
    });
  }
}

/* content script "content.html" */
function toggleEditContent() {
  $("#content").hide();
  $("#image-content").hide();
  $("#input-content")
    .show()
    .val($("#content").html().replace(/<br>/g, "\n"))
    .focus()
    .height($("#content").height());
  $("#button-content").show();
}

function contentSave() {
  const input = $("#input-content");

  if (input.val().length < 2 || input.val().length > 5000) {
    toggleSnackbar("content need to have between 43and 4999 caractes.", "danger");
    return;
  }
  input.hide();
  $("#content").show().html($("#input-content").val().replace(/\r?\n/g, "<br>"));
  $("#image-content").show();
  $("#button-content").hide();
  editTiqet(TIQET_ID, { content: input.val().replace(/<br>/g, "\n") }, (state) => {
    toggleSnackbar(state.status, state.state);
  });
}
