function login() {
    loginData = {
        "username": document.getElementById("username").value,
        "password": document.getElementById("password").value
    }

    sendRequest("/login", "POST", loginResponse, loginData);
}

function loginResponse() {

}