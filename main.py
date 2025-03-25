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
# library.add_book(book_01)


# for x in library.display_books():
#     print(x.title, x.author)

test = [
    {"e0bf19183245d1bf957f345f05a0a99e4478a4b1d9e3f66147119410d913d111": ["Lucas", "de Oliveira", []]},                 {"e0bf19183245d1bf957f345f05a0a99e4478a4b1d9e3f66147119410d913d111": ["Lucas", "de Oliveira", []]},
    {"e0bf19183245d1bf957f345f05a0a99e4478a4b1d9e3f66147119410d913d111": ["Lucas", "de Oliveira", []]}, {"TESTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT": ["Gojo", "Saturo", []]}
        ]

db_user = UserDatabase()
db_user.save_user_info(lucas)

db_user.update_user_database(test)

# name, surname, books = library.find_user(lucas.name, lucas.surname)

# print(name)
# print(surname)
# print(books)


# library.delete_user(name, surname)