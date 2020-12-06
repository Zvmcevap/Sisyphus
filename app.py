from flask import Flask, redirect, url_for, render_template, request, jsonify
import sqlite3
import secrets
import user_class
import json


app=Flask(__name__)
user = user_class.User()

def make_userList():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    with conn:
        userList = []
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM users''')
        users = cursor.fetchall()
        for u in users:
            user = user_class.User(u["user_id"], u["username"], u["password"], u["email"])
            user.check_unique()
            userList.append(user)
        return userList



@app.route('/',methods=['GET','POST'])
def home():
        if user.user_id:
            print("BOOOM")
            return render_template('index.html')
        else:
            return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user.username = request.form["username"]
        user.email = request.form["username"]
        user.password = request.form["password"]
        user.check_unique()

        if user.user_id:
            return redirect(url_for("home"))
        else:
            return jsonify({"error": "Username or Password incorrect"})

        return jsonify({"username" : user.username, "password": user.password})



    else:
        return render_template('login.html')

    


if __name__ == '__main__':
    app.run(debug=True)