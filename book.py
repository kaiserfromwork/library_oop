# Book - class representing the book entity

class Book():
    def __init__(self, title, author, status=False):
        self.title = title
        self.author = author
        self.borrowed = status
        self._book_id = self.create_book_id(title, author)   
    

    def create_book_id(self, title, author):
        return "BOOK ID"                    # TODO: Change to a proper book id


    def get_book_id(self):
        return self._book_id


    def __str__(self):
        return self.title + self.author + self.borrowed