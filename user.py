# User - class representing user entity
# Module Import
import time
import hashlib

# Class Import
from book import Book
from user_database import UserDatabase

class User():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self._id = self.user_id(name, surname)
        self.borrowed_books = []

        if self._id:
            user_info = {
            self._id : [self.name, self.surname, self.borrowed_books]
            }
            UserDatabase.save_user_info(user_info)
        else:
            print(f"{self.name} was not added to database successfully!")



    def user_id(self, name, surname) -> str:
        unique_id = f"{name}{surname}{time.time()}"
        print("ID created!")
        return hashlib.sha256(unique_id.encode()).hexdigest()


    def __str__(self):
        return f"{self.name, self.surname}"