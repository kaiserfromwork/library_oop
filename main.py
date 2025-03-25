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
db_user.save_user_to_database(lucas)

# db_user.update_user_database(test)

# name, surname, books = library.find_user(lucas.name, lucas.surname)

# print(name)
# print(surname)
# print(books)


# library.delete_user(name, surname)