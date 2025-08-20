# library_system.py

class Book:
    """Base class for all books."""

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class for digital books."""

    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # call parent constructor
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class for physical books."""

    def __init__(self, title, author, page_count):
        super().__init__(title, author)  # call parent constructor
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Library class that uses composition to manage books."""

    def __init__(self):
        self.books = []  # list to hold Book, EBook, and PrintBook objects

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)

