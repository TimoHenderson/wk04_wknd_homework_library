import unittest
from models.book import Book


class TestBook(unittest.TestCase):
    def setUp(self):
        self.book_1 = Book("Sound Design", "David Sonnenschein", "Audio")

    def test_has_title(self):
        actual = self.book_1.title
        expected = "Sound Design"
        self.assertEqual(actual, expected)

    def test_has_author(self):
        actual = self.book_1.author
        expected = "David Sonnenschein"
        self.assertEqual(actual, expected)

    def test_has_genre(self):
        actual = self.book_1.genre
        expected = "Audio"
        self.assertEqual(actual, expected)

    def test_has_is_checked_out(self):
        actual = self.book_1.is_checked_out
        expected = False
        self.assertEqual(actual, expected)
