from Flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def init_db():
    with sqlite3.connect('classroom.db') as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS classrooms (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                teacher TEXT NOT NULL
            )
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS assignments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                class_id INTEGER,
                title TEXT,
                description TEXT,
                FOREIGN KEY(class_id) REFERENCES classrooms(id)
            )
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS submissions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                assignment_id INTEGER,
                student TEXT,
                content TEXT,
                FOREIGN KEY(assignment_id) REFERENCES assignments(id)
            )
        ''')

@app.route('/')
def index():
    return render_template('index.html')

# More routes below...

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
