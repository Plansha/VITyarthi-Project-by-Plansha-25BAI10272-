# main.py

from book import Book
from library import Library
from menu import display_menu

def main():
    library = Library()
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            new_book = Book(title, author, isbn)
            library.add_book(new_book)
            print("Book added.")
        elif choice == '2':
            library.list_books()
        elif choice == '3':
            isbn = input("Enter ISBN of book to borrow: ")
            library.borrow_book(isbn)
        elif choice == '4':
            isbn = input("Enter ISBN of book to return: ")
            library.return_book(isbn)
        elif choice == '5':
            query = input("Enter title or author to search: ")
            library.search_book(query)
        elif choice == '6':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
