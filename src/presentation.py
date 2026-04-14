from business import StudentService, SubjectService, GradeService

student_service = StudentService()
subject_service = SubjectService()
grade_service = GradeService()


def menu():
    print("\n===== STUDENT GRADE MANAGEMENT =====")
    print("1. Add student")
    print("2. Add subject")
    print("3. Add grade")
    print("4. View students")
    print("0. Exit")


def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    student_service.add_student(name, age)
    print("Added successfully!")


def add_subject():
    name = input("Enter subject name: ")
    credits = int(input("Enter credits: "))
    subject_service.add_subject(name, credits)
    print("Added successfully!")


def add_grade():
    student_id = int(input("Enter student ID: "))
    subject_id = int(input("Enter subject ID: "))
    score = float(input("Enter score: "))
    grade_service.add_grade(student_id, subject_id, score)
    print("Added successfully!")


def view_students():
    students = student_service.get_all_students()
    print("\n--- Students ---")
    for s in students:
        print(s)


def run():
    while True:
        menu()
        choice = input("Choose: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            add_subject()
        elif choice == "3":
            add_grade()
        elif choice == "4":
            view_students()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")