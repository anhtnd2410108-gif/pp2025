import os
import zipfile

from input import input_students, input_courses, input_marks
from output import list_students, list_courses, show_marks


STUDENT_TXT = "pw5/students.txt"
COURSE_TXT = "pw5/courses.txt"
MARK_TXT = "pw5/marks.txt"
DATA_ZIP = "pw5/students.dat"


def extract_data():
    if os.path.exists(DATA_ZIP):
        with zipfile.ZipFile(DATA_ZIP, "r") as z:
            z.extractall("pw5")


def compress_data():
    with zipfile.ZipFile(DATA_ZIP, "w") as z:
        if os.path.exists(STUDENT_TXT):
            z.write(STUDENT_TXT)
        if os.path.exists(COURSE_TXT):
            z.write(COURSE_TXT)
        if os.path.exists(MARK_TXT):
            z.write(MARK_TXT)


students = []
courses = []
marks = []

extract_data()

while True:
    print("\n===== PW5 Student Management =====")
    print("1. Input students")
    print("2. Input courses")
    print("3. Input marks")
    print("4. List students")
    print("5. List courses")
    print("6. Show marks")
    print("0. Exit")

    choice = input("Choose: ")

    if choice == "1":
        students = input_students()
    elif choice == "2":
        courses = input_courses()
    elif choice == "3":
        marks = input_marks(students, courses)
    elif choice == "4":
        list_students(students)
    elif choice == "5":
        list_courses(courses)
    elif choice == "6":
        cid = input("Course ID: ")
        show_marks(marks, cid)
    elif choice == "0":
        # 🔹 Nén dữ liệu khi thoát
        compress_data()
        print("Data saved to students.dat")
        break
    else:
        print("Invalid choice.")
