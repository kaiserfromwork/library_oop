# Testing Book Class

def test_book_creation(sample_book):
    assert sample_book.title == "1984"
    assert sample_book.author == "George Orwell"
    assert sample_book.year == "1948"


def test_get_book_id(sample_book):
    book_id = sample_book.get_id()
    assert isinstance(book_id, str)
    assert len(book_id) == 64


def test_display_book(sample_book):
    display = sample_book.display_book()
    assert "1984" in display
    assert "George Orwell" in display
    assert "1948" in display


def test_fiction_book_genre(fiction_book):
    assert fiction_book.genre == "Fantasy"
    display = fiction_book.display_book()
    assert "Fantasy" in display


def test_non_fiction_book_genre(non_fiction_book):
    assert non_fiction_book.genre == "Science"
    display = non_fiction_book.display_book()
    assert "Science" in display