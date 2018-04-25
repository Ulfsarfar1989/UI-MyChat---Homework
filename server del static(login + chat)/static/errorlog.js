// JavaScript Document
window.onload = function(){
    function handleinput(){
        if(document.loginform.username.value == "juan"){
            document.getElementById("usernameError").innerHTML = "You must enter a username";
            return false;
        }
 
        if(document.loginform.password.value == "juan"){
            document.getElementById("passwordError").innerHTML = "You must enter a password";
            return false;
        }
    }
 
    document.getElementById("loginform").onsubmit = handleinput;
}