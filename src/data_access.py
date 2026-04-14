import sqlite3

DB_NAME = "school.db"

def get_db_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subject (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            credits INTEGER NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            subject_id INTEGER,
            score REAL NOT NULL,
            FOREIGN KEY (student_id) REFERENCES students(id),
            FOREIGN KEY (subject_id) REFERENCES subject(id)
        )
    ''')
    # Thêm dữ liệu mẫu nếu bảng trống
    cursor.execute("SELECT COUNT(*) FROM students")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("INSERT INTO students (name, age) VALUES (?, ?)",
                           [("Nguyễn Văn An", 16), ("Trần Thị Bình", 17)])
    cursor.execute("SELECT COUNT(*) FROM subject")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("INSERT INTO subject (name, credits) VALUES (?, ?)",
                           [("Toán", 3), ("Văn", 2), ("Anh", 2)])
    conn.commit()
    conn.close()

def get_all_students():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_student_by_id(student_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    row = cursor.fetchone()
    conn.close()
    return row

def get_all_subjects():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subject")
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_subject_by_id(subject_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subject WHERE id = ?", (subject_id,))
    row = cursor.fetchone()
    conn.close()
    return row

def get_subject_credits(subject_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT credits FROM subject WHERE id = ?", (subject_id,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else 0

def add_grade(grade):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO grades (student_id, subject_id, score) VALUES (?, ?, ?)",
                   (grade.student_id, grade.subject_id, grade.score))
    conn.commit()
    conn.close()

def get_grades_by_student(student_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM grades WHERE student_id = ?", (student_id,))
    rows = cursor.fetchall()
    conn.close()
    return rows