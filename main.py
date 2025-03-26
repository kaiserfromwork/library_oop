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


# library.delete_user(lucas)