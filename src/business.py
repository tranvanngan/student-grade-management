from data_access import *

# Tạo class model đơn giản
class Student:
    def __init__(self, id=None, name="", age=0):
        self.id = id
        self.name = name
        self.age = age


class Subject:
    def __init__(self, id=None, name="", credits=0):
        self.id = id
        self.name = name
        self.credits = credits


class Grade:
    def __init__(self, id=None, student_id=0, subject_id=0, score=0):
        self.id = id
        self.student_id = student_id
        self.subject_id = subject_id
        self.score = score


# Service
class StudentService:
    def add_student(self, name, age):
        student = Student(name=name, age=age)
        add_student(student)

    def get_all_students(self):
        return get_all_students()


class SubjectService:
    def add_subject(self, name, credits):
        subject = Subject(name=name, credits=credits)
        add_subject(subject)


class GradeService:
    def add_grade(self, student_id, subject_id, score):
        grade = Grade(student_id=student_id, subject_id=subject_id, score=score)
        add_grade(grade)