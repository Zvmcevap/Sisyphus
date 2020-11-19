# Functions to access and manipulate the User Database
import sqlite3
from user_class import User


conn = sqlite3.connect('database.db')
cursor = conn.cursor()



def insert_user(conn, cursor, user):
    with conn:
        cursor.execute('INSERT INTO users(username, password, email) VALUES (:username, :password, :email)',
                       {"username": user.username, "password": user.password, "email": user.email})
        cursor.execute('SELECT user_id FROM users WHERE username = :username', {"username": user.username})
        user.user_id = cursor.fetchone()[0]


def check_unique(user, userlist):
    for u in userlist:
        if u.username == user.username:
            print("Username taken.")
            return False
        elif u.email == user.email:
            print("Email taken.")
            return False
    return True


def update_userinfo(conn, cursor, user):
    with conn:
        cursor.execute(F'''UPDATE users SET username = :username, password = :password, email = :email
        WHERE user_id = {user.user_id}''', {"username": user.username, "password": user.password, "email": user.email})


def list_users(cursor):
    cursor.execute('SELECT * FROM users ORDER BY username asc')
    tuple_user_list = cursor.fetchall()
    user_obj_list = []
    for u in tuple_user_list:
        user = User(u[1], u[2], u[3])
        user.user_id = u[0]
        user_obj_list.append(user)
    return user_obj_list


def select_user(userlist, user):
    if user.username != "guest":
        for u in userlist:
            if (u.username == user.username or u.email == user.email) and u.password == user.password:
                user.user_id = u.user_id
                user.username = u.username
                user.email = u.email
                print("Login successful")
                return user
    print("Incorrect Login Data")
    return user


def delete_user(conn, cursor, user):
    with conn:
        cursor.execute('DELETE from users WHERE user_id = :user_id', {"user_id": user.user_id})
