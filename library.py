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

     # adds user to library list of users   
    def add_user(self, user: User):
        if isinstance(user, User):
            self.list_of_users.append(user)
            print(f"{user.name} added to library!")
            return True
        else:
            print("Not a valid user!")
            return False
    

    # def delete_user(self, user):
    #     database = self.list_of_users.user_database_info  # storing database as a list 
    #     id = user.get_user_id()
    #     print(id)
    #     print(database[0])
    #     # database.pop(user.get_user_id())

        return True


    def find_user(self, name, surname):
        """Find user based on name and surname
        
        Keyword arguments:
            name (str) -- first name of user
            surname (str) -- last name of user
        
        Return:
            Returns user if in list of users, otherwise returns None
        """
        database = self.list_of_users
        user_id = HashDict.hash_dict(name, surname)
        user = database.user_database_info[0].get(user_id)

        if user:
            print("User Found!")
            return user    
        print("User does not exit")
        return None


    def display_users(self):
        """List users of the library
        
        Return: returns a list  
        """
        
        return self.list_of_users


    # def delete_user(self, name, surname):
    #     user_id = HashDict.hash_dict(name, surname)
    #     new_file = []
    #     try:
    #         with open(FILENAME, "r") as file:
    #             for line in file:
    #                 data = json.loads(line)
    #                 if not data.get(user_id):
    #                     new_file.append(data)
    #         with open(FILENAME, "w") as file:
    #             json.dump(new_file, file)
    #     except(FileNotFoundError, json.JSONDecodeError) as error:
    #         print(f"Error loading user info from database: {error}")
