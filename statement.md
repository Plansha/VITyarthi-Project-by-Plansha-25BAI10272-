Problem statement
The Library Management System is a simple command-line application that helps manage a small collection of books using basic operations such as adding, listing, borrowing, returning, and searching books. It addresses the need for an easy way to track which books are available or borrowed without using a database or complex GUI. The system stores data in a text file so that the library state remains consistent across multiple runs of the program.

Scope of the project
The project is limited to a single-user, local, file-based library system accessed via the terminal. It focuses on core book management operations only and does not include advanced features like user accounts, due dates, fines, or network access. The system is intended as an introductory project demonstrating object-oriented programming, file handling, and basic CLI interaction in Python.

Target users
Students learning Python who want a practical example of OOP and file handling.
Instructors who need a simple demonstration project for teaching basic software development concepts.
Anyone needing a minimal offline tool to track a small set of books on a single machine.

High-level features
Add a book by entering title, author, and ISBN, which is then persisted to a text file.
List all stored books with clear display of title, author, ISBN, and status (Available/Borrowed).
Borrow and return books using their ISBN, updating their status accordingly.
Search for books by title or author using a case-insensitive query from the command-line menu.
