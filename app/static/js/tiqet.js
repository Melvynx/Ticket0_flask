// todo : use font awrsomes
$(document).ready(() => {
  $("#content").html($("#content").html().replace(/\r?\n/g, "<br>"));
  $(".comment-content").each((index, element) => {
    element.innerHTML = element.innerHTML.replace(/\r?\n/g, "<br>");
  });
  $("#title").on("click", toggleEditTitle);
  $("#button-title").on("click", titleSave);
  $("#button-content").on("click", contentSave);
  $("#content").on("click", toggleEditContent);
  $("#button-comment").on("click", sendComment);
  $("#comment").on("keyup", removeShadow);

  initPopper();
});

function initPopper() {
  const ref = document.getElementById("comment");
  const popper = document.getElementById("comment-popper");

  // create the popper
  Popper.createPopper(ref, popper, { placement: "bottom" });
}

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
  const title = $("#input-title");

  if (title.val().length <= 2 || title.val().length >= 100) {
    toggleSnackbar("Title need to have between 2 and 100 caractes.", "danger");
  } else {
    $("#image-title").show();
    title.hide();
    $("#title").html(title.val()).show();
    $("#button-title").hide();
    editTiqet(TIQET_ID, { title: title.val() }, (state) => {
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

  if (input.val().length <= 2 || input.val().length >= 5000) {
    toggleSnackbar("content need to have between 2 and 5000 caractes.", "danger");
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

function sendComment() {
  if ($("#comment").val().length <= 1) {
    $("#comment").css("box-shadow", "0 0 0 0.2rem rgb(220,53,69,0.5)");
    $("#comment-popper").show();
    setTimeout(() => {
      $("#comment-popper").hide();
    }, 2000);
    return;
  }

  const token = getCookie("current-user-token");

  if (!token) {
    toggleSnackbar("You need to be login to post comment.", "danger");
    return;
  }

  const values = {
    comment: {
      user_hash: token ? token : null,
      content: $("#comment").val(),
    },
  };

  const valuesJson = JSON.stringify(values);

  $.ajax({
    url: `${API_URL}/comments/${TIQET_ID}`,
    method: "POST",
    data: valuesJson,
    dataType: "json",
    contentType: "application/json",
    Accept: "application/json",
    success: (status) => {
      if (status.state === "danger") {
        console.warn("Error for post comment : ", status.status);
        return;
      }
      updateComments();
    },
    error: (result) => {
      console.warn("Request status :", result.status);
      console.warn(result.responseJSON);
      toggleSnackbar("Database has problem. Try an other time.", "danger");
    },
  });
}

function updateComments() {
  getComments((comments) => {
    const commentBox = $("#comments");
    commentBox.html("");
    $("#comment").val("");
    comments.map((comment) => {
      const created_at = new Date(comment.created_at);
      const date =
        created_at.toLocaleDateString() + " ," + created_at.toLocaleTimeString();
      commentBox.append(`<div class="d-flex mt-2">
      <div class="">
        <div
          class="usernamme-data rounded-circle d-flex justify-content-center mr-2"
          title="${comment.username}"
        >
          <span>${comment.username.toUpperCase()[0]}</span>
        </div>
      </div>
      <div>
        <div class="text-secondary comment-data">
          <span class="font-weight-bold">${comment.username}</span> •
          <span class="font-italic">${date}</span>
        </div>
        <div class="comment bg-white rounded p-1 mt-1 mr-1 mb-1 d-inline-block">
          <p class="comment-content">${comment.content}</p>  
        </div>
      </div>
    </div>`);
    });
    $(".comment-content").each((index, element) => {
      element.innerHTML = element.innerHTML.replace(/\r?\n/g, "<br>");
    });
  });
}

function getComments(callback) {
  $.ajax({
    url: `${API_URL}/comments/${TIQET_ID}`,
    method: "GET",
    dataType: "json",
    Accept: "application/json",
    success: (comments) => {
      callback(comments);
    },
    error: (result) => {
      console.warn("Request status :", result.status);
      toggleSnackbar("Database has problem. Try an other time.", "danger");
    },
  });
}

function removeShadow() {
  $("#comment").removeAttr("style");
}
