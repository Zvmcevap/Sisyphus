$(document).ready(function () {
  // Sets text to the proper form type
  function logRegUpdate(bol, anim) {
    $("#emaildiv").toggle(anim);
    logRegLabel = bol ? "Login" : "Register";
    usernameLabelText = bol ? "Username or Email" : "Username";
    userInvalidFeedback = bol
      ? "Please enter your username or the email you made up..."
      : "Please enter a username youll forget soon as you login";
    passInvalidFeedback = bol
      ? "We already have all your passwords lol :D"
      : "Please enter the same password you use most everywhere else. All of our data is safely encoded with our unbreakable Benigma (tm) proprietary software.";
    $("#user-invalid-feedback").text(userInvalidFeedback);
    $("#pass-invalid-feedback").text(passInvalidFeedback);
    $("#username_label").text(usernameLabelText);
    $("#login_text").text(`${logRegLabel}`);
    $("#button_login").val(`${logRegLabel}`);
    $("#email").prop("disabled", bol);
  }
  // Then assemble le page
  logRegUpdate(isLogin, 0);

  $(".message a").click(function () {
    isLogin = !isLogin;
    logRegUpdate(isLogin, 1000);
  });

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
          }).done(function (data) {
            console.log(data);
            if (data.error) {
              console.log(data.error);
            } else {
              console.log("Honestly idk");
            }
          });
        }
        form.classList.add("was-validated");
      },
      false
    );
  })();
});
