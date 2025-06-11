# 📚 Library Management System (CLI-based)

A Python-based library management system built with Object-Oriented Programming principles. It supports user registration, borrowing, returning, and reserving items like books, magazines, and DVDs, with data persisted to JSON files for durability.

---

## ✅ How to Run

python main.py

## 🚀 Features

- Register users with unique IDs
- Add, remove, and search for library items (Books, Magazines, DVDs)
- Borrow, return, and reserve items (with error handling)
- Persistent data storage using JSON
- Clean object-oriented design
- Easily extendable and customizable

---

## 🏗️ Project Structure

├── main.py # Entry point for the CLI app

├── controllers/

│ └── LibraryController.py # Manages operations and file persistence

├── models/

│ ├── base/ # Abstract base classes and interfaces

│ ├── Book.py

│ ├── DVD.py

│ ├── Magazine.py

│ ├── User.py

│ └── Library.py

├── exceptions.py # Custom exception classes

├── data/

│ ├── users.json # User data (loaded and saved
at runtime)

│ └── items.json # Library items data

└── README.md
