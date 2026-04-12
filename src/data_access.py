import sqlite3


def get_db_connection():
    return sqlite3.connect("school.db")


def add_student(student):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, age) VALUES (?, ?)", (student.name, student.age)
    )
    conn.commit()
    conn.close()


def get_student_by_id(student_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    row = cursor.fetchone()
    conn.close()
    return row


def delete_student(student_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()


def update_student(student):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE students SET name = ?, age = ? WHERE id = ?",
        (student.name, student.age, student.id),
    )
    conn.commit()
    conn.close()


def get_all_students():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows


def add_subject(subject):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO subject (name, credits) VALUES (?, ?)",
        (subject.name, subject.credits),
    )
    conn.commit()
    conn.close()


def get_subject_by_id(subject_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subject WHERE id = ?", (subject_id,))
    row = cursor.fetchone()
    conn.close()
    return row


def delete_subject(subject_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM subject WHERE id = ?", (subject_id,))
    conn.commit()
    conn.close()


def update_subject(subject):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE subject SET name = ?, credits = ? WHERE id = ?",
        (subject.name, subject.credits, subject.id),
    )
    conn.commit()
    conn.close()


def add_grade(grade):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO grades (student_id, subject_id, score) VALUES (?, ?, ?)",
        (grade.student_id, grade.subject_id, grade.score),
    )
    conn.commit()
    conn.close()


def update_grade(grade):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE grades SET student_id = ?, subject_id = ?, score = ? WHERE id = ?",
        (grade.student_id, grade.subject_id, grade.score, grade.id),
    )
    conn.commit()
    conn.close()


def delete_grade(grade_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM grades WHERE id = ?", (grade_id,))
    conn.commit()
    conn.close()


def get_grade_by_id(grade_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM grades WHERE id = ?", (grade_id,))
    row = cursor.fetchone()
    conn.close()
    return row
