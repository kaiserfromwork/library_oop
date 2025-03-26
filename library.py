# Library 
import json

# classes  import
from book import Book
from user import User
from user_database import UserDatabase
from hash_dict import HashDict



FILENAME = "user_database.json"
class Library():

    def __init__(self):  # Constructor
        self.list_of_users = UserDatabase()
        self.list_of_books = []
    
    
    def add_book(self, book):
        """Adds book to library catalog
        
        Keyword arguments:
            book -- Object of class Book()
        Return: True if book is successfully added and False otherwise

        """
        
        if isinstance(book, Book):  # Checks if book is instance of Book()
            self.list_of_books.append(book)
        else:
            print("Object not of class Book()")
            return False
        
        print(f"Book {book.title} added to the library!")
        return True
    

    def remove_book(self, book: Book):
        """Removes book from list of books owned by Library
        
        Keyword arguments:
            book (obj) -- Object of type Book() 
        
        Return:
            Return 
        """
        
        if isinstance(book, Book): # Checks if book is instance of Book()
            if book in self.list_of_books:
                self.list_of_books.remove(book)
                print("Book removed from Library")
                return True
            
            else:
                print(f"{book.title} is not on the library list.")
                return False
            
        else:
            print(f"Not a instance of Book() class")
            return False    
    

    def display_books(self):
        """Display list of books owned by the Library
        
        Return: 
            Returns list of Books
        """
        
        return self.list_of_books
    
    
    def find_book(self, book_title, book_author):
        """ Finds book in list of books owned by Library
        
        Keyword arguments:
         book_title (str) -- title of book
         book_author (str) -- author of book

        Return: 
            Returns book if in book list, otherwise returns None
        """
        
        for book in self.list_of_books:
            return book if book.title == book_title and book.author == book_author else None

    def borrow_book(self, book_title, user_name):
        pass   
    
    ######## USER ####################################################################################
    
    def delete_user(self, user: User):
        database = self.list_of_users.user_database_info # storing dict database
        id = user.get_user_id()

        if id in database:  # Removes user if in the Database
            database.pop(id)
            UserDatabase.update_user_database(database)
            print("User removed!")
        else:   
            print("User is not on the database!")


    def add_user(self, user: User):
        database = self.list_of_users.user_database_info # Storing dict database
        id = user.get_user_id() # getting user ID

        # Adding user to dict database
        database[id] = {"name": user.name, "surname": user.surname, "books": user.borrowed_books}

        print("User added to database!")

        # Will return True if added, False Otherwise
        return UserDatabase.update_user_database(database)

    
    def find_user(self, name, surname):
        database = self.list_of_users.user_database_info
        id = HashDict.hash_dict(name, surname)

        if id in database:
            print(f"User: {name} {surname} found!")
            return database[id]
        else:
            print(f"Could not find user with name: {name} and surname: {surname}")
            return False
    
