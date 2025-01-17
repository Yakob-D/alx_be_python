class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False  # Default to not checked out

    def check_out(self):
        self.__is_checked_out = True

    def return_book(self):
        self.__is_checked_out = False

    def is_available(self):
        return not self.__is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self.__books = []  # Private list to store books

    def add_book(self, book):
        self.__books.append(book)

    def check_out_book(self, title):
        for book in self.__books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"Checked out: {book.title}")
                return
        print(f"Book '{title}' is not available or does not exist.")

    def return_book(self, title):
        for book in self.__books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"Returned: {book.title}")
                return
        print(f"Book '{title}' was not checked out or does not exist.")

    def list_available_books(self):
        available_books = [book for book in self.__books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(book)
