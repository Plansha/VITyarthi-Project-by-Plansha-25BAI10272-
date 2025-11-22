# library.py

from book import Book
from storage import load_books, save_books

class Library:
    def __init__(self, filename="library_data.txt"):
        self.filename = filename
        self.books = load_books(filename)

    def add_book(self, book):
        self.books.append(book)
        save_books(self.filename, self.books)

    def list_books(self):
        if not self.books:
            print("No books in the library.")
            return
        for book in self.books:
            print(book)

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and not book.is_borrowed:
                book.is_borrowed = True
                print(f"'{book.title}' borrowed successfully.")
                save_books(self.filename, self.books)
                return
        print("Book not found or already borrowed.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.is_borrowed:
                book.is_borrowed = False
                print(f"'{book.title}' returned successfully.")
                save_books(self.filename, self.books)
                return
        print("Book not found or not currently borrowed.")

    def search_book(self, query):
        found_books = [
            book for book in self.books
            if query.lower() in book.title.lower() or query.lower() in book.author.lower()
        ]
        if found_books:
            for book in found_books:
                print(book)
        else:
            print("No books found matching your query.")
