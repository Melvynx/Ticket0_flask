/* title script "title.html" */
function toggleEditTitle() {
  $("#title").hide();
  $("#image-title").hide();
  $("#input-title").show().val($("#title").val()).on("keyup", titleSave).focus();
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
  const content = document.getElementById("content");
  const img = document.getElementById("image-content");
  const input = document.getElementById("input-content");
  const button = document.getElementById("button-content");

  content.classList.add("d-none");
  img.classList.add("d-none");
  input.classList.remove("d-none");
  input.value = content.innerHTML;
  input.addEventListener("keyup", contentSave);
  input.focus();
  button.classList.remove("d-none");
}

function contentSave(event) {
  if (event) if (event.key !== "Enter") return;

  const content = document.getElementById("content");
  const img = document.getElementById("image-content");
  const input = document.getElementById("input-content");
  const button = document.getElementById("button-content");

  if (input.value.length < 2 || input.value.length > 5000) {
    toggleSnackbar("content need to have between 43and 4999 caractes.", "danger");
    return;
  }

  content.classList.remove("d-none");
  img.classList.remove("d-none");
  input.classList.add("d-none");
  content.innerHTML = input.value;
  button.classList.add("d-none");
  editTiqet(TIQET_ID, { content: input.value }, (state) => {
    toggleSnackbar(state.status, state.state);
  });
}
