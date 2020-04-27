$(document).ready(() => {
  $("#submit-form-login").on("click", onSubmit);
});

async function onSubmit() {
  const username = $("#auth-username").val();
  const email = $("#auth-email").val();
  const password = $("#auth-password").val();
  const confirmPassword = $("#auth-conf-password").val();
  let error = "";

  const usernameHelper = checkUsername(username);
  const emailHelper = checkEmail(email);
  const passwordHelper = checkPassword(password);
  const confirmPasswordHelper = checkConfirmPassword(password, confirmPassword);

  if (!confirmPasswordHelper.state) {
    error = confirmPasswordHelper.helper;
  }

  if (!passwordHelper.state) {
    error = passwordHelper.helper;
  }

  if (!emailHelper.state) {
    error = emailHelper.helper;
  }

  if (!usernameHelper.state) {
    error = usernameHelper.helper;
  }

  if (error) {
    $("#auth-helper").text(error).show();
    return;
  }

  credentialStatus = checkCredential(username, email).then((state) => {
    if (!state) {
      return;
    }
    if (!state.username || !state.email) {
      $("#auth-helper").text(state.status).show();
      return;
    }
    console.log("user ok");
  });
}

async function checkCredential(username, email) {
  const credential = { auth: { email: email, username: username } };
  const credentialJson = JSON.stringify(credential);

  return new Promise((resolve) => {
    $.ajax({
      url: `${API_URL}/auth/check_credential`,
      method: "POST",
      data: credentialJson,
      dataType: "json",
      contentType: "application/json",
      Accept: "application/json",
      success: (state) => {
        resolve(state);
      },
      error: (result) => {
        resolve(false);
        console.warn(result.responseJSON);
        toggleSnackbar("Database has problem. Try an other time.", "danger");
      },
    });
  });
}

function checkEmail(email) {
  const reggex = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  const isValidate = reggex.test(email);
  if (!isValidate) {
    return { helper: "Email is not a valid email.", state: false };
  }
  return { helper: "", state: true };
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
