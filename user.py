class User:
    def __init__(self, username, password, email):
        self.user_id = 0
        self.username = username
        self.password = password
        self.email = email
        self.tasks_todo = []
        self.tasks_complete = []
