# book_class.py

class Book:
    """A class representing a book with magic methods for init, del, str, and repr."""

    def __init__(self, title, author, year):
        """Constructor: initializes the Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: called when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """User-friendly string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation (for debugging/recreating the object)."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

