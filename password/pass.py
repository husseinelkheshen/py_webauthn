from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

users = {}

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/register')
def register():
    params = request.args.to_dict()
    pass1 = params["register_password"]
    pass2 = params["register_password2"]
    user = params["register_username"]

    if pass1 == pass2:
        f = open("details.txt", "a")
        f.write(user + "\t" + pass1 + "\n")
        f.close()
        users[user] = pass1
        return "Successfully registered."
    else:
        return "Error! Passwords don't match."

@app.route('/login')
def testing():
    login_params = request.args.to_dict()
    pass_login = login_params["login_password"]
    user_login = login_params["login_username"]

    with open("details.txt") as f:
        for line in f:
           (key, val) = line.split()
           users[key] = val

    if user_login not in users:
        return 'Login failed.'
    elif users[user_login] == pass_login:
        return 'Logged in!'
    else:
        return 'Login failed.'

@app.route('/test')
def dictionary():
    return users

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=4000)
