$(document).ready(function () {
  let isRegister = true;

  $(".message a").click(function () {
    $("#emaildiv").toggle(1000);
    let logRegLabel = isRegister ? "Login" : "Register";
    $("#login_text").text(`${logRegLabel}`);
    $("#button_login").val(`${logRegLabel}`);
    $("#email").prop("required", !isRegister);
    isRegister = !isRegister;
  });

  $("form").on("submit", function (e) {
    e.preventDefault();
    console.log("Submit");
    $.ajax({
      data: $("form").serialize(),
      type: "POST",
      url: isRegister ? "/register" : "/login",
    }).done(function (data) {
      if (data.error) {
        $("#error").html("<p>User data incorrect</p>");
      } else {
        $("#successAlert").text(data.username).show();
      }
    });
  });
});
