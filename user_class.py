import sqlite3

class User():
    def __init__(self,user_id=None, username=None, password=None, email=None):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email

    def check_validity(self):
        conn = sqlite3.connect('database.db')
        conn.row_factory = sqlite3.Row
        with conn:
            cursor = conn.cursor()
            cursor.execute(F'''SELECT user_id FROM users WHERE username = :username AND password= :password OR email = :email AND password= :password
            ''', {"username": self.username, "password": self.password, "email": self.email})
            user_id = cursor.fetchone()
            if user_id:
                user_id = dict(user_id)["user_id"]
            self.user_id = user_id

    def check_unique(self):
        conn = sqlite3.connect('database.db')
        conn.row_factory = sqlite3.Row
        with conn:
            cursor = conn.cursor()
            cursor.execute(f'''SELECT user_id FROM users WHERE username = :username OR email= :email''',
            {"username":self.username, "email": self.email})
            user_ids = cursor.fetchone()
            if user_ids:
                return False
            else:
                return True

    def insert_into_db(self):
        conn = sqlite3.connect('database.db')
        conn.row_factory = sqlite3.Row
        with conn:
            cursor = conn.cursor()
            print(self.username, self.email, self.password)
            cursor.execute(F'''INSERT INTO users (username, password, email) VALUES (:username, :password, :email)
            ''', {"username": self.username, "password": self.password, "email": self.email})
