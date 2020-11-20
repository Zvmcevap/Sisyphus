from flask import Flask, render_template, request, make_response, redirect, url_for, session
import sqlite3
import secrets
from user_class import User
from user_sql_fun import *

# Accessing the Database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create a list of users
user_list = list_users(cursor)
user_1 = User()

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(32)
SESSION_TYPE = 'redis'


@app.route('/')
def index():
    if "user_id" not in session:
        print("Im heere")
        return redirect(url_for("login"))
    else:
        print("Or theeere")
        return make_response(render_template("index.html"), 200, {"Content-Type": "text/html"})


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        session["username"] = request.form['username']
        session["password"] = request.form['password']
        session["user_id"] = None

        user_1 = User(session["username"], session["password"], session["username"])
        user_1 = select_user(user_list, user_1)

        session["user_id"] = user_1.user_id
        print(user_1.user_id)
        if not user_1.user_id:
            print("User_id == None")
            return make_response("Idk, wadaflask", 409)

        else:
            print("User_id != None")
            return redirect(url_for("index"))




if __name__ == '__main__':
    app.run(debug=True)
