# Functions to access and manipulate the User Database

def insert_user(conn, cursor, user):
    with conn:
        cursor.execute('INSERT INTO users(username, password, email) VALUES (:username, :password, :email)',
                       {"username": user.username, "password": user.password, "email": user.email})


def update_username(conn, cursor, user, newname):
    with conn:
        cursor.execute(f'''UPDATE users SET username = :username
        WHERE user_id = {user.user_id}''', {"username": newname})


def update_password(conn, cursor, user, psw):
    with conn:
        cursor.execute(f'''UPDATE users SET username = :username
        WHERE user_id = {user.user_id}''', {"username": psw})


def list_users(cursor):
    cursor.execute('SELECT * from users ORDER BY username asc')
    return cursor.fetchall()


def delete_user(conn, cursor, user):
    with conn:
        cursor.execute('DELETE from users WHERE user_id = :user_id', {"user_id": user.user_id})
