# User - class representing user entity
# Module Import
import time
import hashlib

# Class Import
from book import Book
from OOP.Library_OOP.user_database import UserDatabase

class User():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self._id = self.user_id(name, surname)
        self.borrowed_books = []

        if self._id:
            UserDatabase.save_data()
        else:
            print(f"{self.name} was not added to database successfully!")



    def user_id(self, name, surname) -> str:
        unique_id = f"{name}{surname}{time.time()}"
        return hashlib.sha256(unique_id.encode()).hexdigest()


    def __str__(self):
        return f"{self.name, self.surname}"