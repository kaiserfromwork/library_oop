
# import modules
import json
from datetime import datetime

FILENAME = "borrowed_books_database.json"

class BorrowedBooksDatabase:

    def __init__(self):
        self.borrowed_books_data = self.load_borrowed_books()
        self.list_user_book_index = self.create_user_book_index()


    def load_borrowed_books(self):
        try:
            with open(FILENAME, "r") as file:
                return json.load(file)

        except (FileNotFoundError, json.JSONDecodeError) as error:
            print(f"Error trying to read borrowed books database: {error}")
            return {}



    def update_borrowed_books(self, database):
        try:
            with open(FILENAME, "w") as file:
                json.dump(database, file, indent=4)

            print("Borrowed books database updated!")
            return True
        
        except (json.JSONDecodeError) as error:
            print(f"Error trying to update borrowed books database: {error}")
            return False


    def create_user_book_index(self):
        database = self.borrowed_books_data
        user_book_index_db = {}

        for book_id, data in database.items():
            user_id = data.get('user_id')

            if user_id in user_book_index_db: # Checking if dict[user_id] exists to avoid key error
                user_book_index_db[user_id][book_id] = {str(datetime.now().date())}
            else:
                user_book_index_db[user_id] = {}
        
        return user_book_index_db