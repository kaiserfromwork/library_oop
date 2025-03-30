
import json


FILENAME = "book_database.json"

class BookDatabase:

    def __init__(self):
        self.book_database_info = self.load_book_database()


    def load_book_database(self):
        try:
            with open(FILENAME, "r") as file:
                return json.load(file)
            
        except FileExistsError:
            print(f"Database file: {FILENAME} not found. Initializing an empty database.")
            return {}  
        
        except json.JSONDecodeError as error:
            raise print(f"Error decoding json in {FILENAME}: {error}")
        
        except Exception as error:
            raise print(f"Error while loading database: {FILENAME}: {error}")
        

    def update_book_database(self, book_database):
        try:
            with open(FILENAME, "w") as file:
                json.dump(book_database, file, indent=4)
                
            return True
        except (OSError, json.JSONDecodeError) as error:
            raise (f"Error while writing to {FILENAME}: {error}")