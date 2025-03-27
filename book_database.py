
import json


FILENAME = "book_database.json"

class BookDatabase:

    def __init__(self):
        self.book_database_info = self.load_book_database()


    def load_book_database(self):
        try:
            with open(FILENAME, "r") as file:
                return json.load(file)
            
        except (FileNotFoundError, json.JSONDecodeError) as error:
            print(f"Error trying to read file: {error}")
            return {}
        

    def update_book_database(book_database):
        try:
            with open(FILENAME, "w") as file:
                json.dump(book_database, file, indent=4)
                
            return True
        except (json.JSONDecodeError) as error:
            print(f"Error trying to update file: {error}")
            return False
