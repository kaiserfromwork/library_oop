# Library 
import json

# Database import (JSON Files)
from book_database import BookDatabase
from user_database import UserDatabase

# classes  import
from book import Book
from user import User
from hash_dict import HashDict



FILENAME = "user_database.json"
class Library():

    def __init__(self):  # Constructor
        self.list_of_users = UserDatabase()
        self.list_of_books = BookDatabase()
    
    
    def add_book(self, book: Book):
        database = self.list_of_books.book_database_info
        id =  book.get_book_id()

        database[id] = {"title": book.title, "author": book.author, "year": book.year, "borrowed": book.borrowed}
        BookDatabase.update_book_database(database)

    

    def remove_book(self, book: Book): 
        """Removes books from the database
        
        Keyword arguments:
            book (obj) -- Object of type Book() 
        
        """
        database = self.list_of_books.book_database_info
        id = book.get_book_id()

        if id in database:
            database.pop(id)
            BookDatabase.update_book_database(database)
            print("Book removed from database.")

        else:
            print("Book not on the database.")
    
    
    def find_book(self, title=None): # TODO need to fix this function. not really useful as of now
        database = self.list_of_books.book_database_info

        for book in database.values():
            if title == book['title']:
                print(f"Books is on the database")
            

    def borrow_book(self, book: Book, user: User):
        book_database = self.list_of_books.book_database_info
        user_database = self.list_of_users.user_database_info
        
        # Changing book's status to borrowed and adding book to list of books user is borrowing
        if book.borrowed == False:
            book.borrow_book()
            user.borrowed_books[book.get_book_id()] = \
            {"title": book.title, "author": book.author, "year": book.year, "borrowed": book.borrowed}
            
            print("User successfully borrowed the book")
        else:
            print(f"{book.name} is already being borrowed.")

        book_database[book.get_book_id()] = {"title": book.title, "author": book.author, "year": book.year, "borrowed": book.borrowed}
        user_database[user.get_user_id()] = {"name": user.name, "surname": user.surname, "books": user.borrowed_books}

        BookDatabase.update_book_database(book_database)
        UserDatabase.update_user_database(user_database)




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
    