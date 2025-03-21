# User - class representing user entity

class User():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{self.name, self.surname}"