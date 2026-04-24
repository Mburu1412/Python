class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.borrowed = False

    def borrow_book(self):
        if not self.borrowed:
            self.borrowed = True
            print(f"'{self.title}' has been borrowed.")
        else:
            print(f"'{self.title}' is already borrowed.")

    def return_book(self):
        if self.borrowed:
            self.borrowed = False
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' was not borrowed.")

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.publication_year}, Borrowed: {self.borrowed}")


class LibraryMember:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if isinstance(book, Book):
            self.borrowed_books.append(book)
            book.borrow_book()
            print(f"{self.name} has borrowed '{book.title}'.")
        else:
            print("Invalid book object provided.")

    def return_book(self, book):
        if isinstance(book, Book) and book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.return_book()
            print(f"{self.name} has returned '{book.title}'.")
        elif not isinstance(book, Book):
            print("Invalid book object provided.")
        else:
            print(f"{self.name} did not borrow '{book.title}'.")

    def display_info(self):
        print(f"Member ID: {self.member_id}")
        print(f"Name: {self.name}")
        if self.borrowed_books:
            print("Borrowed Books:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")
        else:
            print("No books currently borrowed.")


# Example Usage:
book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979)
book2 = Book("Pride and Prejudice", "Jane Austen", 1813)

member1 = LibraryMember(101, "Alice Wonderland")

member1.borrow_book(book1)
member1.borrow_book(book2)

member1.display_info()

member1.return_book(book1)

member1.display_info()

book1.display_info()
