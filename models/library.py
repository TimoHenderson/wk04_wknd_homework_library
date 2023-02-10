from models.book import Book


class Library:
    def __init__(self, book_list=[]):
        self.book_list = book_list

    def add_book(self, title, author, genre):
        new_book = Book(title, author, genre)
        self.book_list.append(new_book)

    def remove_book_by_index(self, index):
        return self.book_list.pop(index)

    def check_book_in_or_out(self, index):
        book = self.book_list[index]
        book.is_checked_out = not book.is_checked_out


library = Library(
    [
        Book("Popular Music Culture", "Roy Shuker", "Music", True),
        Book("Sound Design", "David Sonnenschein", "Audio"),
        Book("The Hobbit", "JRR Tolkien", "Fantasy"),
    ]
)
