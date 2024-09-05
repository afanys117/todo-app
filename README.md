# ToDo Web Application

This is a simple ToDo web application built with Flask, SQLite (for database), and basic HTML/CSS/JavaScript for the frontend. The app allows users to add, delete, and mark tasks as completed.

## Features
- Add new tasks
- Mark tasks as completed
- Delete tasks
- SQLite database integration for task persistence

## Prerequisites

- Python 3.11
- Flask

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/username/todo-app.git
   cd todo-app
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/Mac
   # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install flask
   ```

## Running the Application

1. **Run the Flask app:**
   ```bash
   python app.py
   ```

2. Open your web browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

### Note:

- The app automatically creates the `todo.db` SQLite database on the first run, so you don't need to manually create it. The `init_db()` function in `app.py` will handle this.
