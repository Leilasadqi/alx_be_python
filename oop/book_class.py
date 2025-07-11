class Book:
    def __init__(self, title, author, year):
        """Constructor that initializes the book's attributes."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that prints a message when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """User-friendly string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Developer-friendly string representation for recreating the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
