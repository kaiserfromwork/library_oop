# Database
import json

FILENAME = "user_database.json"

class UserDatabase():

    def __init__(self):
        self.load_data()

    def load_data(self):
        try:
            with open(FILENAME, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_data(self):
        pass