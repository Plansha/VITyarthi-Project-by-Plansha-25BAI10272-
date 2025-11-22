# VITyarthi-Project-by-Plansha-25BAI10272-
Project title

Library Management System (Command-Line, Python)

    
Overview

This is a simple command-line Library Management System written in Python.
It lets users add books, list all books, borrow and return books, and search for books by title or author, with data stored in a text file so it persists between runs.

Features

Add new books with title, author, and ISBN.
List all books with their current availability status.
Borrow a book using its ISBN (marks it as borrowed).
Return a borrowed book using its ISBN (marks it as available).
Search books by title or author (case-insensitive search).
Persistent storage of books and their borrowed status in library_data.txt.

Technologies / tools used

Python 3
File handling using a plain text file (library_data.txt)
Object-Oriented Programming (classes Book and Library)
Command-line interface (CLI) using input() and print()

Installation and running the project

1. Prerequisites
Install Python 3 on your system and ensure python or python3 command works in your terminal.
2. Project setup
Create a project folder (for example, library_management).
Save your Python code in a file named main.py (or any name you prefer, but update instructions accordingly).
In the same folder, keep or create library_data.txt (the program will also create it automatically if it does not exist).
3. Run the application
Open a terminal or command prompt in the project folder.
Run:
 On Windows:
 python main.py
On macOS/Linux:
 python3 main.py
The command-line menu will appear, and you can interact with the system by entering the menu choices (1–6).

Instructions for testing

You can test the system manually from the menu:
Add Book
Choose option 1.
Enter a sample title, author, and ISBN.
Confirm that you see the “Book added.” message and that library_data.txt is updated.
List Books
Choose option 2.
Verify that all books are printed with correct title, author, ISBN, and status (“Available” or “Borrowed”).
Borrow Book
Choose option 3.
Enter an existing book’s ISBN.
Check that the message indicates successful borrowing and that listing books now shows the status as “Borrowed”.
Try borrowing the same ISBN again to confirm you get the “Book not found or already borrowed.” message.
Return Book
Choose option 4.
Enter the ISBN of a borrowed book.
Confirm the message shows successful return and the status changes back to “Available”.
Try returning a book that is not borrowed to see the “Book not found or not currently borrowed.” message.
Search Book
Choose option 5.
Enter part or full title or author name.
Verify that matching books are displayed.
Try a keyword that does not exist to see “No books found matching your query.”
Exit
Choose option 6 to exit the application gracefully.

<img width="1920" height="1008" alt="Screenshot 2025-11-22 225420" src="https://github.com/user-attachments/assets/799b536b-3fa3-4dd0-855a-d9e72219f81f" />

<img width="1896" height="927" alt="Screenshot 2025-11-22 225626" src="https://github.com/user-attachments/assets/f355b6fd-b036-4a59-a0b9-fa9c38fd66c7" />

<img width="1875" height="797" alt="Screenshot 2025-11-22 230112" src="https://github.com/user-attachments/assets/21b83a52-1b52-4b16-857d-b0acb2003050" />


