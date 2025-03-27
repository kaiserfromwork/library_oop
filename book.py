# Book - class representing the book entity

# Modules
from hash_dict import HashDict
class Book():
    def __init__(self, title, author, year, borrowed=False):
        self.title = title
        self.author = author
        self.borrowed = borrowed
        self.year = year
        self._book_id = self.create_book_id(title, author, year)   


    def create_book_id(self, title, author, year):
        return HashDict.hash_dict_book(title, author, year)
        
    def borrow_book(self):
        self.borrowed = True


    def get_book_id(self):
        return self._book_id


    def __str__(self):
        return self.title + self.author + self.borrowed