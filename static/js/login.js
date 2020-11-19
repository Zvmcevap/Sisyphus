$(document).ready(function(){

$(".message a").click(function(){
$("form").toggle(1000);
});


$("#button_login").click(function(){
    var username = $("#userlogin").val();
    var password = $("#passlogin").val();

    $.ajax({
        url: '/login',
        data: $('#login_form').serialize(),
        type: 'POST',
        success: function(response) {
            console.log(response);
            },
        error: function(error){
            console.log(error)
            }
        });
    });
return username, password;

});