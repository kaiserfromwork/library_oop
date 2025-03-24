from library import Library
from user import User
from book import Book
from user_database import UserDatabase

# Library
library = Library()

# User
lucas = User("Lucas", "de Oliveira")

# Book
book_01 = Book("1984", "George Orwell")

###################################################### - TEST - ######################################################
library.add_book(book_01)


for x in library.display_books():
    print(x.title, x.author)


# db_user = UserDatabase()
# db_user.save_user_info(lucas)

user_database = library.list_of_users
print(f"Printing Database: \n {user_database}")
# print("")
# print(user_database.user_database_info[0])
# print(type(user_database.user_database_info[0]))
# print("TEST")
# print(user_database.user_database_info[0].get("e0bf19183245d1bf957f345f05a0a99e4478a4b1d9e3f66147119410d913d111"))
# user_test = user_database.user_database_info[0].get("e0bf19183245d1bf957f345f05a0a99e4478a4b1d9e3f66147119410d913d111")
# print(user_test[0])

library.find_user(lucas)