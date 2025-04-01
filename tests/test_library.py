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
    result =  library.delete_user(sample_user)
    assert result is True
    library.user_db.update_user_database.assert_called_once()


# TODO: Finish testing