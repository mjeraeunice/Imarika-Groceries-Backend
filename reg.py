class User:
    def __init__(self):
        self.users = {}

    def login(self, username, password):
        if username not in self.users:
            print("The Username entered does not exist.")
        elif self.users[username] != password:
            print("Incorrect password.")
        else:
            print("Login was successful.")

    def register(self, username, password):
        if username in self.users:
            print("Username already exists.")
        else:
            self.users[username] = password
            print("Registration process was successful.")