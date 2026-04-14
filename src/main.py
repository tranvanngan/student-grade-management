import sys
import os
# Thêm thư mục gốc vào sys.path để import được src
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.data_access import init_db
from src.presentation import display_menu, show_students, show_subjects, input_grade, show_average

def main():
    init_db()
    while True:
        display_menu()
        choice = input("Chọn chức năng (1-5): ")
        if choice == '1':
            show_students()
        elif choice == '2':
            show_subjects()
        elif choice == '3':
            input_grade()
        elif choice == '4':
            show_average()
        elif choice == '5':
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")

if __name__ == "__main__":
    main()