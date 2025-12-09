from input import input_students, input_courses, input_marks
from output import list_students, list_courses, show_marks

students = []
courses = []
marks = []

while True:
    print("\n===== PW4 Student Management =====")
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
        marks.extend(input_marks(students, courses))
    elif choice == "4":
        list_students(students)
    elif choice == "5":
        list_courses(courses)
    elif choice == "6":
        cid = input("Course ID: ")
        show_marks(marks, cid)
    elif choice == "0":
        break
    else:
        print("Invalid choice.")
