class Book:
    def __init__(self, title, author, genre, is_checked_out=False):
        self.title = title
        self.author = author
        self.genre = genre
        self.is_checked_out = is_checked_out
