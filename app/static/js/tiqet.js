// todo : use font awrsomes
$(document).ready(() => {
  $("#content").html($("#content").html().replace(/\r?\n/g, "<br>"));
  $(".comment-content").each((index, element) => {
    element.innerHTML = element.innerHTML.replace(/\r?\n/g, "<br>");
  });
  $("#title").on("click", toggleEditTitle);
  $("#button-title").on("click", () => titleSave());
  $("#button-content").on("click", contentSave);
  $("#content").on("click", toggleEditContent);
  $("#button-comment").on("click", sendComment);
  $("#comment").on("keyup", removeShadow);
  $(".niceSelect").niceSelect();
  autosize($("#input-content"));
  const labelSelect = new Choices(document.getElementById("label-select"), {
    removeItemButton: true,
    itemSelectText: "",
  });

  initLabels((labelsId) => labelSelect.setChoiceByValue(labelsId));

  $("#label-select").on("addItem", addLabel).on("removeItem", removeLabel);

  // .setValue([{ value: "1", label: "Mon chien" }]);

  initPopper();
});

const addLabel = function (label) {
  const label_id = label.detail.id;
  $.ajax({
    url: `${API_URL}/labels/${label_id}/tiqets/${TIQET_ID}`,
    method: "POST",
    dataType: "json",
    Accept: "application/json",
    success: (status) => {
      console.log("done");
    },
  });
};

const removeLabel = function (label) {
  const label_id = label.detail.id;
  $.ajax({
    url: `${API_URL}/labels/${label_id}/tiqets/${TIQET_ID}`,
    method: "DELETE",
    dataType: "json",
    Accept: "application/json",
    success: (status) => {
      console.log("done");
    },
  });
};

const initLabels = function (callback) {
  $.ajax({
    url: `${API_URL}/labels/tiqets/${TIQET_ID}`,
    method: "GET",
    dataType: "json",
    Accept: "application/json",
    success: (labels) => {
      if (labels.length === 0) return;
      callback(labels.map((label) => String(label.id_label)));
    },
  });
};

const initPopper = function () {
  const ref = document.getElementById("comment");
  const popper = document.getElementById("comment-popper");

  // create the popper
  Popper.createPopper(ref, popper, { placement: "bottom" });
};

/* title script "title.html" */
const toggleEditTitle = function () {
  $("#title").hide();
  $("#image-title").hide();
  $("#input-title").show().val($("#title").html()).on("keyup", titleSave).focus();
  $("#button-title").show();
};

const titleSave = function (event) {
  if (event) if (event.key !== ("Enter" | undefined)) return;

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
};

/* content script "content.html" */
const toggleEditContent = function () {
  $("#content").hide();
  $("#image-content").hide();
  $("#input-content")
    .show()
    .val($("#content").html().replace(/<br>/g, "\n"))
    .focus()
    .height($("#content").height());
  $("#button-content").show();
};

const contentSave = function () {
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
};

const sendComment = function () {
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
      console.warn(
        `Request status : ${result.status}, request state:`,
        result.responseJSON
      );
      toggleSnackbar("Database has problem. Try an other time.", "danger");
    },
  });
};

const updateComments = function () {
  getComments((comments) => {
    const commentBox = $("#comments").html("");
    $("#comment").val("");
    comments.forEach((comment) => commentBox.append(generateComment(comment)));
  });
};

const generateComment = function (comment) {
  const date = new Date(comment.created_at);
  const dateString = date.toLocaleDateString() + " ," + date.toLocaleTimeString();

  const usernameContainer = $(document.createElement("div"))
    .addClass("usernamme-data rounded-circle d-flex justify-content-center mr-2")
    .append(
      $(document.createElement("span")).text(comment.username.toUpperCase()[0])
    );

  const dataContainer = $(document.createElement("div"))
    .addClass("text-secondary comment-data")
    .append(
      $(document.createElement("span"))
        .addClass("font-weight-bold")
        .text(comment.username)
    )
    .append(
      $(document.createElement("span")).addClass("font-italic").text(dateString)
    );

  const commentText = $(document.createElement("div"))
    .addClass("comment bg-white rounded p-1 mt-1 mr-1 mb-1 d-inline-block")
    .append(
      $(document.createElement("p"))
        .addClass("comment-content")
        .text(comment.content.replace(/\r?\n/g, "<br>"))
    );

  const commentContainer = $(document.createElement("div"))
    .append(dataContainer)
    .append(commentText);

  return $(document.createElement("div"))
    .addClass("d-flex mt-2")
    .append(usernameContainer)
    .append(commentContainer);
};

const getComments = function (callback) {
  $.ajax({
    url: `${API_URL}/comments/${TIQET_ID}`,
    method: "GET",
    dataType: "json",
    Accept: "application/json",
    success: (comments) => {
      callback(comments);
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

const removeShadow = function () {
  $("#comment").removeAttr("style");
};
