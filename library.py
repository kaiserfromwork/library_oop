# Library 
from book import Book

class Library():

    def __init__(self):
        self.list_of_users = []
        self.list_of_books = []


    def add_book(self, book):
        if isinstance(book, Book):
            self.list_of_books.append(book)
        else:
            return "Object not of class Book()"
        return f"Book {book.title} added to the library!"
    

    def remove_book(self, book):
        if isinstance(book, Book):
            if book in self.list_of_books:
                self.list_of_books.remove(book)
            else:
                return f"{book.title} is not on the library list."
        else:
            return "Not a instance of Book() class"
    

    def display_users(self):
        return self.list_of_users
    

    def display_books(self):
        return self.list_of_books
    
    
    def find_user(self, name, surname):
        for user in self.list_of_users:
            if user.name == name and user.surname == surname:
                return user
        return None
    
    
    def find_book(self, book_name, book_author):
        for book in self.list_of_books:
            return book if book.name == book_name and book.author == book_author else None
