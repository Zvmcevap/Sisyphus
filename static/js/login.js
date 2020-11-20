$(document).ready(function(){
$(".message a").click(function(){
$("form").toggle(1000);
});


$("#button_login").click(function(){

    $.ajax({
        url: '/login',
        data: $('#login_form').serialize(),
        type: 'POST',
        success: function(response) {
            document.write(response);
            },
        error: function(error){
            if (!$('#inc').length) {
            $("#fg-pass").append("<p id='inc' style='color: red'> Incorrect Login info </p>");
            }
            }
        });
    });
return username, password;

});