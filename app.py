from flask import Flask, render_template, request, make_response
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from user import User
from user_sql_fun import *

# Accessing the Database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

list1 = list_users(cursor)
for x in list1:
    print(x)
    user_del = User(x[1], x[2], x[3])
    user_del.user_id = x[0]
    delete_user(conn, cursor, user_del)

user_1 = User("Beno2", "dsad", "Beno@gmm.cm")
user_2 = User("Matic", "2134", "mat.cat@tat.at")
user_3 = User("Dean", "2112", "Zupko_moneymaker@gmail.com")

list_u = [user_1, user_2, user_3]
for u in list_u:
    insert_user(conn, cursor, u)

list1 = list_users(cursor)

print(list1)

for x in list1:
    print(x)
