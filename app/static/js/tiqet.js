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
  button.classList.remove("d-none");
}

function titleSave() {
  const title = document.getElementById("title");
  const img = document.getElementById("image-title");
  const input = document.getElementById("input-title");
  const button = document.getElementById("button-title");

  if (input.value.length < 3 || input.value.length > 50) {
    toggleSnackBar("Title need to have between 4 and 49 caractes.");
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
