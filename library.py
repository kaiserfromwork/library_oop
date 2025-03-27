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

        database[id] = {"title": book.title, "author": book.author, "borrowed": book.borrowed}
        BookDatabase.update_book_database(database)

    

    def remove_book(self, book: Book): #TODO Implement remove book function
        """Removes book from list of books owned by Library
        
        Keyword arguments:
            book (obj) -- Object of type Book() 
        
        Return:
            Return 
        """
        database = self.list_of_books.book_database_info
        id = book.get_book_id()
        print(f"ID: {id}")

        if id in database:
            database.pop(id)
            BookDatabase.update_book_database(database)
            print("Book removed from database.")

        else:
            print("Book not on the database.")
    
    
    def find_book(self, book_title, book_author): # TODO Implement function
        """ Finds book in list of books owned by Library
        
        Keyword arguments:
         book_title (str) -- title of book
         book_author (str) -- author of book

        Return: 
            Returns book if in book list, otherwise returns None
        """
        
        for book in self.list_of_books:
            return book if book.title == book_title and book.author == book_author else None

    def borrow_book(self, book_title, user_name): # TODO implement function, maybe create a new JSON file for books borrowed
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
    