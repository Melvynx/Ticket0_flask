/* title script "title.html" */
function toggleEditTitle() {
  const title = document.getElementById("title");
  const img = document.getElementById("image-title");
  const input = document.getElementById("input-title");
  const button = document.getElementById("button-title");

  title.classList.add("d-none");
  img.classList.add("d-none");
  input.classList.remove("d-none");
  input.value = title.innerHTML;
  input.addEventListener("keyup", titleSave);
  input.focus();
  button.classList.remove("d-none");
}

function titleSave(event) {
  if (event) if (event.key !== "Enter") return;

  const title = document.getElementById("title");
  const img = document.getElementById("image-title");
  const input = document.getElementById("input-title");
  const button = document.getElementById("button-title");

  if (input.value.length < 3 || input.value.length > 50) {
    toggleSnackBar("Title need to have between 4 and 49 caractes.", "danger");
    return;
  }

  title.classList.remove("d-none");
  img.classList.remove("d-none");
  input.classList.add("d-none");
  title.innerHTML = input.value;
  button.classList.add("d-none");
  editTiqet(TIQET_ID, { title: input.value }, (state) => {
    toggleSnackBar(state.status, state.state);
  });
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
    toggleSnackBar("content need to have between 43and 4999 caractes.", "danger");
    return;
  }

  content.classList.remove("d-none");
  img.classList.remove("d-none");
  input.classList.add("d-none");
  content.innerHTML = input.value;
  button.classList.add("d-none");
  editTiqet(TIQET_ID, { content: input.value }, (state) => {
    toggleSnackBar(state.status, state.state);
  });
}
