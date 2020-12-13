from flask import Flask, redirect, url_for, render_template, request, jsonify, make_response, session
import sqlite3
from os import path
import secrets
import user_class
import json
from passlib.hash import sha256_crypt


app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(32)


def make_userlist():
    the_list = []
    ROOT = path.dirname(path.realpath(__file__))
    conn = sqlite3.connect(path.join(ROOT, "database.db"))
    conn.row_factory = sqlite3.Row
    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        query = cursor.fetchall()
        print(query)
    for row in query:
        r = dict(row)
        usr = user_class.User(r["user_id"], r["username"],
                              r["password"], r["email"])
        the_list.append(usr)
    return the_list


@app.route('/')
def home():
    if "user_id" in session:
        user = user_class.User(user_id=session["user_id"])
        user.get_user_by_id()
        if user.username == "admin":
            return redirect(url_for("userlist"))
        return render_template('index.html', user=user)
    else:
        return render_template('index.html')


@app.route('/user/<string:name>')
def logged_home(name):
    user = user_class.User(user_id=session["user_id"])
    user.get_user_by_id()
    if user.user_id == 51:
        return redirect(url_for("userlist"))

    else:
        return render_template('index.html', user=user)


@app.route('/userlist')
def userlist():
    users = make_userlist()
    return render_template("userlist.html", users=users)


@app.route('/login', methods=['GET', 'POST'])
def login():
    user = user_class.User()
    if request.method == 'POST':
        user.username = request.form["username"]
        user.email = request.form["username"]
        password_candidate = request.form["password"]
        user.check_username()
        if sha256_crypt.verify(password_candidate, user.password):
            user.get_user_by_id()
            session['user_id'] = user.user_id
            return url_for("home")
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

        password_candidate = request.form["password"]
        user.password = sha256_crypt.hash(password_candidate)

        if user.check_unique():
            user.insert_into_db()
            user.check_username()
            session['user_id'] = user.user_id
            session['username'] = user.username
            return url_for("home")
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
