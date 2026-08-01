import pytest
from library import Library


def test_add_book():
    library = Library()
    library.add_book("Python Basics")
    assert "Python Basics" in library.books


def test_remove_existing_book():
    library = Library()
    library.add_book("Python Basics")
    library.remove_book("Python Basics")
    assert "Python Basics" not in library.books


def test_remove_non_existing_book():
    library = Library()

    with pytest.raises(ValueError):
        library.remove_book("Java")


def test_search_existing_book():
    library = Library()
    library.add_book("Python Basics")
    assert library.search_book("Python Basics") is True


def test_search_missing_book():
    library = Library()
    assert library.search_book("Java") is False


def test_duplicate_book_not_added():
    library = Library()
    library.add_book("Python Basics")
    library.add_book("Python Basics")

    assert len(library.books) == 1