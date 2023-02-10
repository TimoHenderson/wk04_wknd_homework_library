from models.book import Book


class Library:
    def __init__(self, book_list=[]):
        self.book_list = book_list

    def add_book(self, title, author, genre):
        new_book = Book(title, author, genre)
        self.book_list.append(new_book)
