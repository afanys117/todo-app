from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            status INTEGER NOT NULL DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

# Route for the home page
@app.route('/')
def index():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('SELECT * FROM tasks')
    tasks = c.fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

# Route for adding new tasks
@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('INSERT INTO tasks (task) VALUES (?)', (task,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# Route for deleting tasks
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# Route for marking tasks as complete
@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('UPDATE tasks SET status = 1 WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
