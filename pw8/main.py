from domains.student import Student
from domains.course import Course
from domains.mark import Mark
from persistence import save_data, load_data

students, courses, marks = load_data()
save_thread = None

while True:
    print("\n===== PW8 Multithreaded Student Management =====")
    print("1. Input students")
    print("2. Input courses")
    print("3. Input marks")
    print("4. List students")
    print("5. List courses")
    print("6. Show marks")
    print("0. Exit")

    choice = input("Choose: ")

    if choice == "1":
        students.clear()
        n = int(input("Number of students: "))
        for _ in range(n):
            s = Student()
            s.input()
            students.append(s)

    elif choice == "2":
        courses.clear()
        n = int(input("Number of courses: "))
        for _ in range(n):
            c = Course()
            c.input()
            courses.append(c)

    elif choice == "3":
        cid = input("Course ID: ")
        for s in students:
            m = float(input(f"Mark for {s.get_id()}: "))
            marks.append(Mark(cid, s.get_id(), m))

    elif choice == "4":
        for s in students:
            s.show()

    elif choice == "5":
        for c in courses:
            c.show()

    elif choice == "6":
        cid = input("Course ID: ")
        for m in marks:
            if m.course_id == cid:
                print(f"{m.student_id}: {m.mark}")

    elif choice == "0":
        print("Saving data in background...")
        save_thread = save_data(students, courses, marks)
        break

    else:
        print("Invalid choice.")

if save_thread:
    save_thread.join()
