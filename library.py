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

    def __init__(self, user_db, books_db, borrowed_books_db):  # Constructor
        self.user_db = user_db
        self.books_db = books_db
        self.borrowed_books_db = borrowed_books_db
    
    
    def add_book(self, book: Book):
        """Adds book to database
        
        Keyword arguments:
            book (Book) -- book (obj)
            
        """
        try:
            database = self.books_db.book_database_info  # storing database
            book_id =  book.get_book_id() # getting book id

            # adding changes to database
            database[book_id] = {"title": book.title, "author": book.author, "year": book.year} 
            self.books_db.update_book_database(database)
            return True
        
        except Exception as error:
            print(f"Error while trying to add book to database: {error}")
            return False

    

    def remove_book(self, book: Book): 
        """Removes books from the database
        
        Keyword arguments:
            book (obj) -- Object of type Book() 
        
        """
        try:
            database = self.books_db.book_database_info
            book_id = book.get_book_id()

            if book_id in database:
                database.pop(book_id)
                self.books_db.update_book_database(database)
                return True
            else:
                return False
            
        except Exception as error:
            print(f"Error trying to remove book from database: {error}")
            return False

    
    def find_book(self, title, author, year): 
        database = self.books_db.book_database_info
        book_id = HashDict.hash_dict_book(title, author, year)

        if book_id in database:
            return database[book_id]
        else:
            return None
        

    def borrow_book(self, book: Book, user: User):
        """User borrows book
        
        Keyword arguments:
            book (Book) -- Book(obj)
            user (User) -- User(obj)            
        """
        
        try: 
            borrowed_book_database = self.borrowed_books_db.borrowed_books_data      
            book_id = book.get_book_id()

            if book_id in borrowed_book_database:
                return False
            else:
                borrowed_book_database[book_id] = {"user_id":  user.get_user_id(), "date": str(datetime.now().date())}  
                # Updating database (JSON file)
                self.borrowed_books_db.update_borrowed_books(borrowed_book_database)
                # Updating in-memory database
                self.borrowed_books_db.create_user_book_index()
                return True

        except Exception as error:
            print(f"Error trying to borrow book: {error}")
            return False    
        

    def return_book(self, book: Book):
        try:
            borrowed_book_database = self.borrowed_books_db.borrowed_books_data
            book_id = book.get_book_id()

            if book_id in borrowed_book_database:
                borrowed_book_database.pop(book_id)
                
                # Updating in-memory database
                self.books_db.create_user_book_index(borrowed_book_database)
                return True
            else: 
                return False
            
        except Exception as error:
            print(f"Error trying to return book: {error}")
        


    ######## USER ####################################################################################

    def delete_user(self, user: User):
        """Deletes user from database
        
        Keyword arguments:
            user (User) -- user (obj)
        
        """
        
        database = self.user_db.user_database_info # storing dict database
        id = user.get_user_id()

        if id in database:  # Removes user if in the Database
            database.pop(id)
            self.user_db.update_user_database(database)
            return True
        else:   
            return False

    def add_user(self, user: User):
        """Adds user to database
        
        Keyword arguments:
            user (User) -- User(obj)
        
        """
        try:
            database = self.user_db.user_database_info # Storing dict database
            id = user.get_user_id() # getting user ID

            # Adding user to dict database
            database[id] = {"name": user.name, "surname": user.surname}
            self.user_db.update_user_database(database)
            return True
        
        except Exception as error:
            print(f"Error trying to add user to database: {error}")
            

    
    def find_user(self, name, surname):
        """Finds if user is on the database
        
        Keyword arguments:
            name (str) -- name used to find user
            surname (str) -- surname used to find user
        Return: 
            Returns used if found and false if not found!
        """
        try:
            database = self.user_db.user_database_info
            id = HashDict.hash_dict(name, surname)

            if id in database:
                return database[id]
            else:
                return None
        
        except Exception as error:
            print(f"Error trying to find user: {error}")
    