# User - class representing user entity
from book import Book

class User():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.borrowed_books = []

 
    def __str__(self):
        return f"{self.name, self.surname}"