# 📚 Book Logger Web App

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Flask](https://img.shields.io/badge/Flask-Backend-green?style=flat&logo=flask)
![Frontend](https://img.shields.io/badge/Frontend-HTML%2FCSS%2FJS-orange?style=flat)

A clean, modern web application designed to help track and manage your reading list. This project has evolved from a simple Python command-line script into a **full-stack web application** featuring a Flask REST API backend and a responsive HTML/CSS/JS frontend.

It tracks books across three distinct categories: **Completed**, **Currently Reading**, and **Planned**.

## ✨ Features

* **Auto-Launch:** The application automatically opens your default web browser when started.
* **Kanban-style Tracking:** View your books categorized into three clear columns.
* **REST API Backend:** Uses Python Flask to handle data requests (GET, POST).
* **State Management:** Move books between statuses (e.g., from *Planned* to *Reading*) using an intuitive dropdown menu.
* **Persistent Data:** All data is automatically saved to local text files (`.txt`) in a `Book Logs` directory.

## 🛠️ Tech Stack

* **Backend:** Python 3, Flask, Flask-CORS
* **Frontend:** HTML5, CSS3, Vanilla JavaScript (Fetch API)
* **Data Storage:** Plain Text Files (Flat-file storage)

## 🚀 Installation and Setup

### Prerequisites

You need **Python 3.x** installed on your system.

### 1. Clone and Setup

Clone the repository and navigate to the project root:

```bash
git clone [https://github.com/Wiruden/BookLogger](https://github.com/Wiruden/BookLogger)
cd BookLogger
````

### 2\. Install Dependencies

You will need to install `Flask` and `Flask-CORS`:

```bash
pip install flask flask-cors
```

### 3\. Run the Application

Navigate to the `python` directory and start the script. This will start the local server and **automatically launch the GUI** in your web browser.

```bash
cd python
python app.py
```

*You should see a message in the terminal saying "Server is running on port 5000..." and your browser will pop up automatically.*

## 📖 Usage Guide

1.  **Add a Book:** Type a book title in the input box at the top and click **"Log Book"**. It will appear in the "Planned" column.
2.  **Manage a Book:** Click the pencil icon (✎) next to any book title to open the action menu.
      * **Move:** Select a new category (e.g., "Move to Reading") to transfer the book.
      * **Delete:** Remove the book permanently from your logs.
3.  **Data Persistence:** You can close the browser or stop the server; your data remains saved in the `python/Book Logs` folder.

## 📂 Project Structure

```text
BookLogger/
│
├── python/                 # Backend Logic
│   ├── app.py              # The Flask API (handles auto-launch)
│   └── Book Logs/          # Generated automatically
│       ├── Completed_Books_Log.txt
│       ├── Reading_Books_Log.txt
│       └── Planned_Books_Log.txt
│
├── website/                # Frontend Interface
│   ├── index.html          # Main webpage
│   ├── style.css           # Styling
│   └── script.js           # API connections
│
├── .gitignore
└── README.md
```

## 🛣️ ROADMAP

  * **Executable Creation:** Bundle into a `.exe` using Auto-Py-To-Exe for simpler distribution.
  * **Database Integration:** Migrate from `.txt` files to SQLite.
  * **Book Metadata:** Integrate with Google Books API for cover art.

-----

*Created by Wiruden*
