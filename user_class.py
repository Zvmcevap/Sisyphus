class User:
    def __init__(self, username="guest", password="123", email="guest@guest.com"):
        self.user_id = 0
        self.username = username
        self.password = password
        self.email = email
        self.tasks_todo = []
        self.tasks_complete = []
