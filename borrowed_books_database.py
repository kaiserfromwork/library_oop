
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
            return {}
            # raise (f"Error while reading {FILENAME}: {error}")



    def update_borrowed_books(self, database):
        try:
            with open(FILENAME, "w") as file:
                json.dump(database, file, indent=4)
            return True
        
        except (json.JSONDecodeError) as error:
            raise (f"Error while writing to {FILENAME}: {error}")
                      



    def create_user_book_index(self):
        database = self.borrowed_books_data
        user_book_index_db = {}

        for book_id, data in database.items():
            user_id = data.get('user_id')
            borrowed_date = data.get('date')

            if user_id in user_book_index_db: # Checking if dict[user_id] exists to avoid key error
                user_book_index_db[user_id][book_id] = {borrowed_date}
            else:
                user_book_index_db[user_id] = {}
        
        return user_book_index_db