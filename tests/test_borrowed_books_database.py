# TESTING

from borrowed_books_database import BorrowedBooksDatabase


def test_create_user_book_index():
    db = BorrowedBooksDatabase()
    test_data = {
        "book1": {"user_id": "user1", "date": "2025-03-31"},
        "book2": {"user_id": "user2", "date": "2025-03-31"},
        "book3": {"user_id": "user3", "date": "2025-03-31"}
    }

    db.borrowed_books_data = test_data
    index = db.create_user_book_index()

    assert "user1" in index
    assert "book1" in index["user1"]
    assert "book2" in index["user2"]
    assert "user2" in index
    assert "book3" in index["user2"]