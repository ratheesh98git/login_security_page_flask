from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  

users = {
    "Ratheesh": generate_password_hash("12345678"),
    "arun": generate_password_hash("123"),
    "akash": generate_password_hash("123"),
}

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    if 'username' in session:
        return render_template('home.html')
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/authenticate', methods=['POST'])
def authenticate():
    username = request.form['username']
    password = request.form['password']

    if username in users and check_password_hash(users[username], password):
        session['username'] = username
        return redirect(url_for('home'))
    else:
        return render_template('login.html', error="Invalid username or password")

if __name__ == '__main__':
    app.run(debug=True)
