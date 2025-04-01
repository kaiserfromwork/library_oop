import pytest
from book import Book, FictionBook, NonFictionBook
from user import User, StudentUser, StaffUser


@pytest.fixture
def sample_book():
    return Book("1984", "George Orwell", "1948")

@pytest.fixture
def fiction_book():
    return FictionBook("The Hobbit", "JRR Tolkien", "1937", "Fantast")

@pytest.fixture
def non_fiction_book():
    return NonFictionBook("Thinking, Fast and Slow", "Daniel Kahneman", "2011" ,"Science")

@pytest.fixture
def sample_user():
    return User("John", "Doe")


@pytest.fixture
def student_user():
    return StudentUser("Jane", "Doe", "Computer Science")

@pytest.fixture
def staff_user():
    return StaffUser("Peter", "Park", "Director")