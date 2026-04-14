from src.data_access import (
    get_grades_by_student,
    get_subject_credits,
    add_grade as data_add_grade,
    get_student_by_id,
    get_subject_by_id
)
from src.models import Grade

def add_grade(student_id: int, subject_id: int, score: float) -> None:
    if score < 0 or score > 10:
        raise ValueError("Điểm phải nằm trong khoảng 0 đến 10")
    student = get_student_by_id(student_id)
    if not student:
        raise ValueError(f"Học sinh với id {student_id} không tồn tại")
    subject = get_subject_by_id(subject_id)
    if not subject:
        raise ValueError(f"Môn học với id {subject_id} không tồn tại")
    grade = Grade(id=None, student_id=student_id, subject_id=subject_id, score=score)
    data_add_grade(grade)

def calculate_average_score(student_id: int) -> float:
    grades = get_grades_by_student(student_id)
    if not grades:
        return 0.0
    total_weight = 0
    total_score = 0.0
    for grade in grades:
        subject_id = grade[2]   # tuple: (id, student_id, subject_id, score)
        score = grade[3]
        credits = get_subject_credits(subject_id)
        total_weight += credits
        total_score += score * credits
    if total_weight == 0:
        return 0.0
    return round(total_score / total_weight, 2)