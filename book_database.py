
import json


FILENAME = "book_database.json"

class BookDatabase:

    def __init__(self):
        self.book_database_info = self.load_book_database()


    def load_book_database(self):
        try:
            with open(FILENAME, "r") as file:
                return json.load(file)
            
        except FileNotFoundError:
            print(f"Database file: {FILENAME} not found. Initializing an empty database.")
            return {}  
        
        except json.JSONDecodeError as error:
            print(f"Error decoding json in {FILENAME}: {error}")
            raise

        except Exception as error:
            print(f"Error while loading database: {FILENAME}: {error}")
            raise

    def update_book_database(self, book_database):
        """Updates json file (FILENAME) database.
        
        Keyword arguments:
            database(dict) -- dict used to updated json file database.
       
         Return: 
            returns true if file is updated and raises an error otherwise. 
        """
        try:
            with open(FILENAME, "w") as file:
                json.dump(book_database, file, indent=4)
                
            return True
        except (OSError, json.JSONDecodeError) as error:
            raise (f"Error while writing to {FILENAME}: {error}")