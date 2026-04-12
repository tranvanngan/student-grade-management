# src/models.py
class Student:
    def __init__(self, id: int, name: str, class_name: str):
        self.id = id
        self.name = name
        self.class_name = class_name

class Subject:
    def __init__(self, id: int, name: str, credits: int):
        self.id = id
        self.name = name
        self.credits = credits

class Grade:
    def __init__(self, id: int, student_id: int, subject_id: int, score: float):
        self.id = id
        self.student_id = student_id
        self.subject_id = subject_id
        self.score = score
