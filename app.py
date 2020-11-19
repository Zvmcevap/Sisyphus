from flask import Flask, render_template, request, make_response, redirect, url_for, json
import sqlite3
from user_class import User
from user_sql_fun import *

# Accessing the Database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create a list of users
user_list = list_users(cursor)

app = Flask(__name__)
user_a = User()

@app.route('/')
def first_page():
    print(user_a.username)
    if user_a.username == "guest":
        return redirect(url_for("login"))
    else:
        return render_template("index.html")


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        user_a = User(username, password, username)
        print("User first: ", user_a.username, user_a.password, user_a.email)
        user_a = select_user(user_list, user_a)
        print("User second", user_a.username, user_a.password, user_a.email)

        if user_a.username == "guest":
            return make_response("User does not exist", 409)

        else:
            return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
