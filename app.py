from flask import Flask, redirect, url_for, render_template, request, jsonify, make_response, session
import sqlite3
import secrets
import user_class
import json


app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(32)


@app.route('/')
def home():
    if "user_id" in session:
        user = user_class.User(user_id=session["user_id"])
        user.get_user_by_id()
        return redirect(url_for("logged_home"))
    else:
        return render_template('index.html')


@app.route('/user/<string:name>')
def logged_home(name):
    user = user_class.User(user_id=session["user_id"])
    user.get_user_by_id()
    return render_template('index.html', user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    user = user_class.User()
    if request.method == 'POST':
        user.username = request.form["username"]
        user.email = request.form["username"]
        user.password = request.form["password"]
        user.check_validity()
        user.get_user_by_id()

        if user.user_id:
            session['user_id'] = user.user_id

            return url_for("logged_home", name=user.username)
        else:
            return 'Invalid user information', 400

    else:
        return render_template('login.html', isLogin=True)


@app.route('/register', methods=['POST', 'GET'])
def register():
    user = user_class.User()
    if request.method == 'POST':
        user.username = request.form["username"]
        user.email = request.form["email"]
        user.password = request.form["password"]
        if user.check_unique():
            user.insert_into_db()
            user.check_validity()
            session['user_id'] = user.user_id
            return url_for("logged_home", name=user.username)
        else:
            return "Username or email taken", 403

    else:
        return render_template('login.html', isLogin=False)


@app.route('/logout')
def logout():
    session.pop("user_id", None)
    return redirect(url_for("home"))


@app.route('/about')
def aboutPage():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
