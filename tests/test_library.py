import pytest
from library import Library
from book import Book
from user import User

@pytest.fixture
def library():

    # creating mock database
    user_db = pytest.Mock()
    book_db = pytest.Mock()
    borrowed_book_db = pytest.Mock()


    # Initialize library with mock database
    return Library(user_db, book_db, borrowed_book_db)


@pytest.fixture
def sample_book():
    return Book("1984", "George Orwell", "1948")


def sample_user():
    return User("John", "Doe")


def test_add_user(library, sample_user):
    library.user_db.user_database_info = {}
    library.add_user(sample_user)
    library.user_db.update_user_database.assert_called_once()


def test_find_user(library, sample_user):
    library.user_db.user_database_info = {sample_user.get_user_id(): {"name": "John", "surname": "Doe"}}
    result =  library.find_user(sample_user)
    assert result is True
    library.user_db.update_user_database.assert_called_once()


def test_delete_user(library, sample_user):
    library.user_db.user_database_info = {sample_user.get_user_id(): {"name": "John", "surname": "Doe"}}
    result =  library.delete_user(sample_user)
    assert result is True
    library.user_db.update_user_database.assert_called_once()


def test_add_book(library, sample_book):
    library.books_db.book_database_info = {}
    result = library.add_book(sample_book)
    assert result is True
    library.books_db.update_book_database.assert_called_once()


def test_remove_book(library, sample_book):
    library.books_db.book_database_info = {sample_book.get_book_id(): {"title": "1984", "author": "George Orwell", "year": "1948"}}
    result = library.remove_book(sample_book)
    assert result is True
    library.books_db.update_book_database.assert_called_once()


def test_find_book(library, sample_book):
    library.books_db.book_database_info = {sample_book.get_book_id(): {"title": "1984", "author": "George Orwell", "year": "1948"}}
    result = library.find_book("1984", "George Orwell", "1948")
    assert result == {"title": "1984", "author": "George Orwell", "year": "1948"}


def test_borrow_book(library, sample_book, sample_user):
    library.borrowed_books_db.borrowed_books_data = {}
    result = library.borrow_book(sample_book, sample_user)
    assert result is True
    library.borrowed_books_db.update_borrowed_books.assert_called_once()

def test_return_book(library, sample_book):
    library.borrowed_books_db.borrowed_books_data = {sample_book.get_book_id(): {"user_id": "user1", "date": "2023-01-01"}}
    result = library.return_book(sample_book)
    assert result is True
    library.borrowed_books_db.update_borrowed_books.assert_called_once()