# Book - class representing the book entity

# Modules
from hash_dict import HashDict
class Book():
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self._book_id = self.create_book_id(title, author, year)   


    def create_book_id(self, title, author, year):
        return HashDict.hash_dict_book(title, author, year)
        

    def get_book_id(self):
        return self._book_id
    

    def display_book(self):
        return (f"tile : {self.title}, author: {self.author}, year: {self.year}")


    def __str__(self):
        return self.title + self.author + self.year 

class FictionBook(Book):

    def __init__(self, title, author, year, genre="Fiction"):
        super().__init__(title, author, year)
        self.genre = genre


    def display_book(self):
        parent_class = super().display_book()

        return f"{parent_class}, genre : {self.genre}"