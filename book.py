# Book - class representing the book entity

class Book():
    def __init__(self, title, author, status=False):
        self.title = title
        self.author = author
        self.status = status
    

    def __str__(self):
        return self.title + self.author + self.status