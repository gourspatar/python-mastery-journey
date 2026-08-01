import unittest
from library import Library


class TestLibrary(unittest.TestCase):

    def test_add_book(self):
        library = Library()
        library.add_book("Python Basics")
        self.assertIn("Python Basics", library.books)

    def test_remove_existing_book(self):
        library = Library()
        library.add_book("Python Basics")
        library.remove_book("Python Basics")
        self.assertNotIn("Python Basics", library.books)

    def test_remove_non_existing_book(self):
        library = Library()

        with self.assertRaises(ValueError):
            library.remove_book("Java")

    def test_search_existing_book(self):
        library = Library()
        library.add_book("Python Basics")
        self.assertTrue(library.search_book("Python Basics"))

    def test_search_missing_book(self):
        library = Library()
        self.assertFalse(library.search_book("Java"))

    def test_duplicate_book_not_added(self):
        library = Library()
        library.add_book("Python Basics")
        library.add_book("Python Basics")

        self.assertEqual(len(library.books), 1)


if __name__ == "__main__":
    unittest.main()