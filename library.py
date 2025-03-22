# Library 
from book import Book

class Library():

    def __init__(self):  # Constructor
        self.list_of_users = []
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
    

    def remove_book(self, book):
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

    def display_users(self):
        """List users of the library
        
        Return: returns a list  
        """
        
        return self.list_of_users
    

    def display_books(self):
        """Display list of books owned by the Library
        
        Return: 
            Returns list of Books
        """
        
        return self.list_of_books
    
    
    def find_user(self, name, surname):
        """Find user based on name and surname
        
        Keyword arguments:
            name (str) -- first name of user
            surname (str) -- last name of user
        
        Return:
            Returns user if in list of users, otherwise returns None
        """
        
        for user in self.list_of_users:
            if user.name == name and user.surname == surname:
                return user
        return None
    
    
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
