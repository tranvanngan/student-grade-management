import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS subject (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    credits INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    subject_id INTEGER,
    score REAL
)
""")

conn.commit()
conn.close()