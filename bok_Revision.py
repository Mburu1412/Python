class Book:
    """
    Represents a book in the library management system.
    """

    def __init__(self, title: str, author: str, publication_year: int):
        """
        Initializes a new Book object.

        Args:
            title: The title of the book.
            author: The author of the book.
            publication_year: The year the book was published.
        """
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.borrowed = False  # Initially, the book is not borrowed

    def borrow_book(self):
        """
        Marks the book as borrowed.
        """
        if not self.borrowed:
            self.borrowed = True
            print(f"'{self.title}' has been borrowed.")
        else:
            print(f"'{self.title}' is already borrowed.")

    def return_book(self):
        """
        Marks the book as returned.
        """
        if self.borrowed:
            self.borrowed = False
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' was not borrowed.")

    def display_info(self):
        """
        Displays the book's information.
        """
        status = "Borrowed" if self.borrowed else "Available"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication Year: {self.publication_year}")
        print(f"Status: {status}")
        print("-" * 20)

# Create a new book
book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979)

# Display its initial information
book1.display_info()

# Borrow the book
book1.borrow_book()
book1.display_info()

# Try to borrow it again
book1.borrow_book()

# Return the book
book1.return_book()
book1.display_info()
