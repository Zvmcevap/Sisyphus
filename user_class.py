import sqlite3
from os import path



class User():
    def __init__(self,user_id=None, username=None, password=None, email=None):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email


    def check_username(self):
        ROOT = path.dirname(path.realpath(__file__))
        conn = sqlite3.connect(path.join(ROOT, "database.db"))
        conn.row_factory = sqlite3.Row
        with conn:
            cursor = conn.cursor()
            cursor.execute('SELECT user_id, password FROM users WHERE username = :username OR email = :email',
            {"username": self.username, "email": self.email})
            info = cursor.fetchone()
            if info:
                user_id = dict(info)["user_id"]
                password = dict(info)["password"]
                
            self.user_id = user_id
            self.password = password

    def check_unique(self):
        ROOT = path.dirname(path.realpath(__file__))
        conn = sqlite3.connect(path.join(ROOT, "database.db"))
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
        ROOT = path.dirname(path.realpath(__file__))
        conn = sqlite3.connect(path.join(ROOT, "database.db"))
        conn.row_factory = sqlite3.Row
        with conn:
            cursor = conn.cursor()
            print(self.username, self.email, self.password)
            cursor.execute(F'''INSERT INTO users (username, password, email) VALUES (:username, :password, :email)
            ''', {"username": self.username, "password": self.password, "email": self.email})


    def get_user_by_id(self):
        ROOT = path.dirname(path.realpath(__file__))
        conn = sqlite3.connect(path.join(ROOT, "database.db"))
        conn.row_factory = sqlite3.Row
        with conn:
            cursor = conn.cursor()
            cursor.execute('''SELECT username, email, password FROM users WHERE user_id = :user_id''', {"user_id": self.user_id})
            fetched_data = cursor.fetchone()
            if fetched_data:
                fetched_data = dict(fetched_data)
                self.username = fetched_data["username"]
                self.email = fetched_data["email"]
                self.password = fetched_data["password"]