import unittest
from models.library import Library
from models.book import Book


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.empty_library = Library()

        self.book_list = [
            Book("Popular Music Culture", "Roy Shuker", "Music"),
            Book("Sound Design", "David Sonnenschein", "Audio", True),
            Book("The Hobbit", "JRR Tolkien", "Fantasy"),
        ]

        self.full_library = Library(self.book_list)

    def test_has_book_list__empty(self):
        actual = self.empty_library.book_list
        expected = []
        self.assertEqual(actual, expected)

    def test_has_book_list__not_empty(self):
        actual = self.full_library.book_list
        expected = self.book_list
        self.assertEqual(actual, expected)

    def test_can_add_book(self):
        self.full_library.add_book("The Gruffalo", "Julia Donaldson", "Children")
        actual_book = self.full_library.book_list[-1]
        actual_title = actual_book.title
        expected_title = "The Gruffalo"
        self.assertEqual(actual_title, expected_title)
        actual_author = actual_book.author
        expected_author = "Julia Donaldson"
        self.assertEqual(actual_author, expected_author)
        actual_genre = actual_book.genre
        expected_genre = "Children"
        self.assertEqual(actual_genre, expected_genre)

    def test_can_remove_book_by_index(self):
        expected_book = self.book_list[2]
        actual_book = self.full_library.remove_book_by_index(2)
        self.assertEqual(actual_book, expected_book)
        actual_length = len(self.full_library.book_list)
        expected_length = 2
        self.assertEqual(actual_length, expected_length)

    def test_can_check_book_in(self):
        self.full_library.check_book_in_or_out(1)
        actual = self.full_library.book_list[1].is_checked_out
        expected = False
        self.assertEqual(actual, expected)

    def test_can_check_book_out(self):
        self.full_library.check_book_in_or_out(0)
        actual = self.full_library.book_list[0].is_checked_out
        expected = True
        self.assertEqual(actual, expected)

    def test_can_check_book_in__already_checked_in(self):
        self.full_library.check_book_in_or_out(0, False)
        actual = self.full_library.book_list[0].is_checked_out
        expected = False
        self.assertEqual(actual, expected)
