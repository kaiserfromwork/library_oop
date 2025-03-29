# Library 
import json
from datetime import datetime

# Database import (JSON Files)
from book_database import BookDatabase
from user_database import UserDatabase
from borrowed_books_database import BorrowedBooksDatabase

# classes  import
from book import Book
from user import User
from hash_dict import HashDict



FILENAME = "user_database.json"
class Library():

    def __init__(self):  # Constructor
        self.list_of_users = UserDatabase()
        self.list_of_books = BookDatabase()
        self.list_of_borrowed_books = BorrowedBooksDatabase()
    
    
    def add_book(self, book: Book):
        """Adds book to database
        
        Keyword arguments:
            book (Book) -- book (obj)
            
        """
        
        database = self.list_of_books.book_database_info  # storing database
        book_id =  book.get_book_id() # getting book id

        # adding changes to database
        database[book_id] = {"title": book.title, "author": book.author, "year": book.year} 
        
        BookDatabase.update_book_database(database)

    

    def remove_book(self, book: Book): 
        """Removes books from the database
        
        Keyword arguments:
            book (obj) -- Object of type Book() 
        
        """
        database = self.list_of_books.book_database_info
        book_id = book.get_book_id()

        if id in database:
            database.pop(book_id)
            BookDatabase.update_book_database(database)
            print("Book removed from database.")

        else:
            print("Book not on the database.")
    
    
    def find_book(self, title, author, year): 
        database = self.list_of_books.book_database_info
        book_id = HashDict.hash_dict_book(title, author, year)

        if book_id in database:
            return database[book_id]
        else:
            print("Book not found!")
            return False
        
            

    def borrow_book(self, book: Book, user: User):
        """User borrows book
        
        Keyword arguments:
            book (Book) -- Book(obj)
            user (User) -- User(obj)            
        """
        
        borrowed_book_database = self.list_of_borrowed_books.borrowed_books_data      
        book_id = book.get_book_id()

        if book_id in borrowed_book_database:
            print(f"Book: {book.title} already being borrowed.")
            return False
        else:
            borrowed_book_database[book_id] = {"user_id":  user.get_user_id(), "date": str(datetime.now().date())}  

            # Updating database (JSON file)
            BorrowedBooksDatabase.update_borrowed_books(borrowed_book_database)
            # Updating in-memory database
            BorrowedBooksDatabase.create_user_book_index()
        




    ######## USER ####################################################################################

    def delete_user(self, user: User):
        """Deletes user from database
        
        Keyword arguments:
            user (User) -- user (obj)
        
        """
        
        database = self.list_of_users.user_database_info # storing dict database
        id = user.get_user_id()

        if id in database:  # Removes user if in the Database
            database.pop(id)
            UserDatabase.update_user_database(database)
            print("User removed!")
        else:   
            print("User is not on the database!")


    def add_user(self, user: User):
        """Adds user to database
        
        Keyword arguments:
            user (User) -- User(obj)
        
        """
        database = self.list_of_users.user_database_info # Storing dict database
        id = user.get_user_id() # getting user ID

        # Adding user to dict database
        database[id] = {"name": user.name, "surname": user.surname}

        UserDatabase.update_user_database(database)

    
    def find_user(self, name, surname):
        """Finds if user is on the database
        
        Keyword arguments:
            name (str) -- name used to find user
            surname (str) -- surname used to find user
        Return: 
            Returns used if found and false if not found!
        """
        
        database = self.list_of_users.user_database_info
        id = HashDict.hash_dict(name, surname)

        if id in database:
            print(f"User: {name} {surname} found!")
            return database[id]
        else:
            print(f"Could not find user with name: {name} and surname: {surname}")
            return False
    