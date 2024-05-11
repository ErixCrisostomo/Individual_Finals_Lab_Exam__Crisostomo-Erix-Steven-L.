import os
from .user import User

class UserManager:
    def __init__(self):
        self.users = {}
        self.load_users()

    def load_users(self):
        if not os.path.exists("data"):
            os.makedirs("data")
        if not os.path.exists("data/users.txt"):
            with open("data/users.txt", "w"):
                pass
        with open("data/users.txt", "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                self.users[username] = User(username, password)

    def save_users(self):
        with open("data/users.txt", "w") as file:
            for user in self.users.values():
                file.write(f"{user.username},{user.password}\n")

    def validate_username(self, username):
        return username in self.users

    def validate_password(self, password):
        return len(password) >= 8

    def register(self, username, password):
        self.users[username] = User(username, password)
        self.save_users()
        print("Registration Successful.")

    def login(self, username, password):
        if username in self.users and self.users[username].password == password:
            return self.users[username]
        else:
            print("Invalid Username or Password.")
            return None