
# import modules
import json
from datetime import datetime

FILENAME = "borrowed_books_database.json"

class BorrowedBooksDatabase:

    def __init__(self):
        self.borrowed_books_data = self.load_borrowed_books()
        self.list_user_book_index = self.create_user_book_index()


    def load_borrowed_books(self):
        """Loads stored data in json file (FILENAME)
        
        Return: 
            Returns data from json file database if file exists, returns an empty {} to initialize a new database if file doesn't exits
            and raise errors in case an unexpected error occurs
        """
        
        try:
            with open(FILENAME, "r") as file:
                return json.load(file)

        except FileExistsError:
            print(f"Database file: {FILENAME} not found. Initializing an empty database.")
            return {}  
        
        except json.JSONDecodeError as error:
            print(f"Error decoding json in {FILENAME}: {error}")
            raise

        except Exception as error:
            print(f"Error while loading database: {FILENAME}: {error}")
            raise


    def update_borrowed_books(self, database):
        """Updates json file (FILENAME) database.
        
        Keyword arguments:
            database(dict) -- dict used to updated json file database.
       
         Return: 
            returns true if file is updated and raises an error otherwise. 
        """
        
        try:
            with open(FILENAME, "w") as file:
                json.dump(database, file, indent=4)
            return True
        
        except (OSError, json.JSONDecodeError) as error:
            raise (f"Error while writing to {FILENAME}: {error}")
                      



    def create_user_book_index(self):
        """Creates a inverted index in-memory to keep track of borrowed books
        
        Keyword arguments:
            Return: returns an inverted index list based on borrowed books database e.g.(user_id = {book_id_01, book_id_02})
        """
        
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