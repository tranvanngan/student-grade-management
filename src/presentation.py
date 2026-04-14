from src.data_access import get_all_students, get_all_subjects
from src.business import add_grade, calculate_average_score

def display_menu():
    print("\n=== HỆ THỐNG QUẢN LÝ ĐIỂM HỌC SINH ===")
    print("1. Xem danh sách học sinh")
    print("2. Xem danh sách môn học")
    print("3. Nhập điểm cho học sinh")
    print("4. Tính điểm trung bình của học sinh")
    print("5. Thoát")

def show_students():
    students = get_all_students()
    if not students:
        print("Chưa có học sinh nào.")
    else:
        print("\nDanh sách học sinh:")
        for s in students:
            print(f"ID: {s[0]} | Tên: {s[1]} | Tuổi: {s[2]}")

def show_subjects():
    subjects = get_all_subjects()
    if not subjects:
        print("Chưa có môn học nào.")
    else:
        print("\nDanh sách môn học:")
        for sub in subjects:
            print(f"ID: {sub[0]} | Tên: {sub[1]} | Tín chỉ: {sub[2]}")

def input_grade():
    try:
        student_id = int(input("Nhập ID học sinh: "))
        subject_id = int(input("Nhập ID môn học: "))
        score = float(input("Nhập điểm (0-10): "))
        add_grade(student_id, subject_id, score)
        print("Đã lưu điểm thành công!")
    except ValueError as e:
        print(f"Lỗi: {e}")

def show_average():
    try:
        student_id = int(input("Nhập ID học sinh: "))
        avg = calculate_average_score(student_id)
        print(f"Điểm trung bình của học sinh ID {student_id} là: {avg}")
    except ValueError:
        print("ID không hợp lệ.")