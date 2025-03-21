from library import Library
from user import User
from book import Book

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