$(document).ready(function () {
  let logRegLabel;
  let usernameLabelText;
  let userNamePlaceholder;
  let userInvalidFeedback;
  let passInvalidFeedback;
  let switchMessage;
  let alertMessage;
  // Sets text to the proper form type
  function logRegUpdate(bol, anim) {
    $("#emaildiv").toggle(anim);
    logRegLabel = bol ? "Login" : "Register";
    usernameLabelText = bol ? "Username or Email" : "Username";
    userNamePlaceholder = bol ? "Username / Email" : "Username";
    userInvalidFeedback = bol
      ? "Please enter your username or the email you made up..."
      : "Please enter a username youll forget soon as you login";
    passInvalidFeedback = bol
      ? "We already have all your passwords lol :D"
      : "Please enter the same password you use most everywhere else. All of our data is safely encoded with our unbreakable Benigma (tm) proprietary software.";
    switchMessage = bol
      ? 'Not registered? <a href="#" class="switch">Create an account</a>'
      : 'Have an account? <a href="#" class="switch">Login here</a>';
    alertMessage = bol
      ? '<button type="button" class="close">&times;</button><strong>Username or Password</strong> incorrect!<br />Would you rather <a href="#" class="alert-link switch">create an account?</a>.'
      : '<button type="button" class="close">&times;</button><strong>Username or Email</strong> taken!<br />Would you rather <a href="#" class="alert-link switch">Login instead?</a>.';
    $(".message").html(switchMessage);
    $("#username").attr("placeholder", userNamePlaceholder);
    $("#user-invalid-feedback").text(userInvalidFeedback);
    $("#pass-invalid-feedback").text(passInvalidFeedback);
    $("#username_label").text(usernameLabelText);
    $("#login_text").text(`${logRegLabel}`);
    $("#button_login").val(`${logRegLabel}`);
    $("#email").prop("disabled", bol);
    $(".alert").html(alertMessage);
  }

  // Assemble page depending on its Type
  logRegUpdate(isLogin, 0);

  // Switch Between Forms
  $(document).on("click", "a.switch", function () {
    isLogin = !isLogin;
    $(".alert").hide(500);
    $("#button_login").addClass("mt-5");
    logRegUpdate(isLogin, 1000);
  });

  // Alert hiding
  $(document).on("click", ".close", function () {
    $(".alert").hide(500);
    $("#button_login").addClass("mt-5");
  });
  // Submition
  (function () {
    "use strict";
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var form = document.querySelector(".needs-validation");
    // Do the submit magic
    form.addEventListener(
      "submit",
      function (event) {
        form.classList.remove("was-validated");
        event.preventDefault();
        if (!form.checkValidity()) {
          event.stopPropagation();
        } else {
          $.ajax({
            data: $("form").serialize(),
            type: "POST",
            url: isLogin ? "/login" : "/register",

            error: function (response) {
              console.log("Le fail");
              $(".alert").show();
              $("#button_login").removeClass("mt-5");
            },
            success: function (response) {
              console.log(response);
            },
          });
        }
        form.classList.add("was-validated");
      },
      false
    );
  })();
});
