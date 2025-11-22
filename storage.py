# storage.py

from book import Book

def load_books(filename):
    books = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                data = line.strip().split(',')
                if len(data) == 4:
                    book = Book(data[0], data[1], data[2], data[3] == 'True')
                    books.append(book)
    except FileNotFoundError:
        pass  # No file yet, return empty list
    return books

def save_books(filename, books):
    with open(filename, 'w') as f:
        for book in books:
            f.write(f"{book.title},{book.author},{book.isbn},{book.is_borrowed}\n")
