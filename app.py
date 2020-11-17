from flask import Flask, render_template, request, make_response
import sqlite3
from user_class import User
from user_sql_fun import *

# Accessing the Database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create a list of users
user_list = list_users(cursor)

app = Flask(__name__)


@app.route('/')
def first_page():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)