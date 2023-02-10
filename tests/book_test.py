import unittest
from models.book import Book


class TestBook(unittest.TestCase):
    def setUp(self):
        self.book_1 = Book("Sound Design")

    def test_has_title(self):
        actual = self.book_1.title
        expected = "Sound Design"
        self.assertEqual(actual, expected)
