$(document).ready(() => {
  $("#save-button").on("click", onSave);
});

function onSave() {
  const newPassword = $("#new-password").val();
  const newPasswordConfirm = $("#new-password-confirm").val();
  const newPasswordHelper = checkPassword(newPassword);
  const newPasswordConfirmHelper = checkConfirmPassword(
    newPassword,
    newPasswordConfirm
  );

  if (!newPasswordHelper.state) {
    $("#auth-helper").show().text(newPasswordHelper.helper);
    return;
  }

  if (!newPasswordConfirmHelper.state) {
    $("#auth-helper").show().text(newPasswordConfirmHelper.helper);
    return;
  }

  const token = getCookie("current-user-token");

  const newValues = {
    auth: {
      old_password: $("#old-password").val(),
      new_password: newPassword,
      user_cookie: token ? token : null,
    },
  };

  const newValuesJson = JSON.stringify(newValues);
  $.ajax({
    url: `${API_URL}/auth/password/${USER_ID}`,
    method: "PATCH",
    data: newValuesJson,
    dataType: "json",
    contentType: "application/json",
    Accept: "application/json",
    success: (state) => {
      toggleSnackbar(state.status, state.state);
      if (state.state === "success") {
      }
    },
    error: (result) => {
      console.warn(
        `Request status : ${result.status}, request state:`,
        result.responseJSON
      );
      toggleSnackbar("Database has problem. Try an other time.", "danger");
    },
  });
}

function checkPassword(password) {
  const reggex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z]{8,}$/;
  const isValidate = reggex.test(password);

  if (!isValidate) {
    return {
      helper:
        "Passowrd need to have : 1 uppercase and lowercase letter, 1 number, 8 caracteres.",
      state: false,
    };
  }
  return { helper: "", state: true };
}

function checkConfirmPassword(password, confirmPassword) {
  if (password !== confirmPassword) {
    return { helper: "Confirm password doesn't match with password.", state: false };
  }
  return { helper: "", state: true };
}

function checkUsername(username) {
  if (username.length > 20 || username.length < 3) {
    return {
      helper: "Username need to have between 3 and 20 caracteres.",
      state: false,
    };
  }
  return { helper: "", state: true };
}
