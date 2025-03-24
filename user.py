# User - class representing user entity
# Module Import
import time

# Class Import
from book import Book
from user_database import UserDatabase
from hash_dict import HashDict
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
        return HashDict(name, surname)


    def __str__(self):
        return f"{self.name, self.surname}"