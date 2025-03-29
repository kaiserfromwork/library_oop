
# import modules
import json


FILENAME = "borrowed_books_database.json"

class BorrowedBooksDatabase:

    def __init__(self):
        self.borrowed_books_data = self.load_borrowed_books()
        self.list_users_books= self.load_users_books()


    def load_borrowed_books(self):
        try:
            with open(FILENAME, "r") as file:
                json.load(file)

        except (FileNotFoundError, json.JSONDecodeError) as error:
            print(f"Error trying to read borrowed books database: {error}")



    def update_borrowed_books(self, database):
        try:
            with open(FILENAME, "w") as file:
                json.dump(database, file, indent=4)

            print("Borrowed books database updated!")
            return True
        
        except (json.JSONDecodeError) as error:
            print(f"Error trying to update borrowed books database: {error}")
            return False


    def load_users_books():
        pass