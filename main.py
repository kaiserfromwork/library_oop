# import Database
from user_database import UserDatabase
from book_database import BookDatabase
from borrowed_books_database import BorrowedBooksDatabase


# Import Modules
from library import Library
from user import User
from book import Book

# Initiating

# Database
user_db = UserDatabase()
books_db = BookDatabase()
borrowed_book_db = BorrowedBooksDatabase()


# Library - (Dependency Injection )
library = Library(user_db, books_db, borrowed_book_db)


# User
lucas = User("Lucas", "de Oliveira")
elric = User("Edward", "Elric")

# Book
book_01 = Book("1984", "George Orwell", "1948")
book_02 = Book("Pride and Prejudice", "Jane Austen", "1813")

###################################################### - TEST - ######################################################
library.add_user(lucas)
library.add_user(elric)

print(library.find_user("Lucas", "de Oliveira"))
# print(library.display_user_list)
# library.delete_user(lucas)

library.add_book(book_01)
library.add_book(book_02)
# library.remove_book(book_01)

library.borrow_book(book_01, lucas)
library.borrow_book(book_02, lucas)
library.find_book("1984", "George Orwell", "1948")
library.find_user("Lucas", "de Oliveira")

# library.return_book(book_01)