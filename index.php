<!DOCTYPE html>
<html>
<head>
    <title>Login Form</title>
</head>
<body>
    <h2>Login Page</h2>
    <form action="/login" method="POST" id="loginForm">
        <label for="username">Username:</label><br>
        <input type="text" id="username" name="username"><br>
        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password"><br><br>
        <input type="submit" value="Login">
    </form>

    <script>
        document.getElementById('loginForm').onsubmit = function() {
            var username = document.getElementById('username').value;
            var password = document.getElementById('password').value;
            console.log('Username: ' + username);
            console.log('Password: ' + password);
        }
    </script>
</body>
</html>

