class Student:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

class Subject:
    def __init__(self, id, name, credits):
        self.id = id
        self.name = name
        self.credits = credits

class Grade:
    def __init__(self, id, student_id, subject_id, score):
        self.id = id
        self.student_id = student_id
        self.subject_id = subject_id
        self.score = score
