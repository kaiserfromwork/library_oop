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
        """Adds book to database
        
        Keyword arguments:
            book (Book) -- book (obj)
            
        """
        
        database = self.list_of_books.book_database_info  # storing database
        id =  book.get_book_id() # getting book id

        # adding changes to database
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
    
    
    def find_book(self, title, author, year): 
        database = self.list_of_books.book_database_info

        
            

    def borrow_book(self, book: Book, user: User):
        """User borrows book
        
        Keyword arguments:
            book (Book) -- Book(obj)
            user (User) -- User(obj)            
        """
        
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
        database[id] = {"name": user.name, "surname": user.surname, "books": user.borrowed_books}

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
    