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
        self._id = self.create_user_id(name, surname)

    # use this func to get protected self._id of the user
    def get_user_id(self):
        return str(self._id)
    

    def create_user_id(self, name, surname):
        return HashDict.hash_dict(name, surname)


    def display_user(self):
        return (f"Name: {self.name}, Surname: {self.surname}")


    def __str__(self):
        return (f"Name: {self.name}, Surname: {self.surname}, id: {self._id}")
    

class StudentUser(User):

    def __init__(self, name, surname, faculty):
        super().__init__(name, surname)
        self.faculty = faculty


    def display_student(self):
        parent_display = super().display_user()
        return (f"{parent_display}, Faculty: {self.faculty}")


class StaffUser(User):

    def __init__(self, name, surname, position):
        super().__init__(name, surname)
        self.position = position
    

    def display_staff(self):
        parent_display = super().display_user()
        return (f"{parent_display}, position: {self.position}")