from library import Library
from user import User
from book import Book
from user_database import UserDatabase

# Library
library = Library()

# User
lucas = User("Lucas", "de Oliveira")
elric = User("Edward", "Elric")

# Book
book_01 = Book("1984", "George Orwell")

###################################################### - TEST - ######################################################
db_user = UserDatabase()
library.add_user(lucas)
library.add_user(elric)

print(library.find_user("Lucas", "de Oliveira"))
# print(library.display_user_list)
library.delete_user(lucas)

library.add_book(book_01)