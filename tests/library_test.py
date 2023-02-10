import unittest
from models.library import Library


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.empty_library = Library()

    def test_has_book_list__empty(self):
        actual = self.empty_library.book_list
        expected = []
        self.assertEqual(actual, expected)
