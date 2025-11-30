# 📚 Python Command-Line Book Logger

A simple command-line Python application designed to help track and manage your reading list across three distinct categories: **Completed**, **Currently Reading**, and **Planned**.

This project demonstrates core Python skills including file I/O operations, string manipulation, input validation, and code refactoring.

## ✨ Features

The Book Logger provides a command-line interface with the following functions:

* **Log a Book:** Add a new book to the Completed, Reading, or Planned log files.
* **Edit Pages:** Update the number of pages read for a book in the "Reading" log using regular expressions (`re`).
* **Delete a Book:** Remove an entry from any of the three log files.
* **View a File:** Display the numbered contents of any of the three log files.
* **Move a Book:** Transfer an entry from one status list to another (e.g., from Planned to Reading), demonstrating advanced function reuse.
* **Persistent Data:** All data is saved automatically to local `.txt` files.

## 🛠️ Installation and Setup

### Prerequisites

You need **Python 3.x** installed on your system.

### How to Run

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/Wiruden/BookLogger
    cd BookLogger
    ```
2.  **Run the Script:**
    ```bash
    python bookLogger.py
    ```

The program will automatically create a directory named `Book Logs` in the same folder, containing the three `.txt` log files.

## 📖 Usage Example

When you run the script, you will be prompted with a menu:

    ```bash
    1. Log a book 2. Delete a book 3. Edit pages 4. View a file 5. Move a book (Press 'X' to exit):



## 🛣️ Future Enhancements

* **Search Functionality:** Implement a tool to search all logs for a specific title.
* **GUI Migration: Convert the application into a desktop application using Tkinter or another framework.