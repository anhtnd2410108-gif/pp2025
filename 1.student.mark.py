# Student Mark Management Program

students = []
courses = []
marks = {}  # key: course_id, value: {student_id: mark}


# ---------------------------
# Input Functions
# ---------------------------

def input_students():
    n = int(input("Enter number of students: "))
    for _ in range(n):
        print("\n--- Enter student info ---")
        sid = input("Student ID: ")
        name = input("Student name: ")
        dob = input("Date of birth: ")

        students.append({
            "id": sid,
            "name": name,
            "dob": dob
        })


def input_courses():
    n = int(input("Enter number of courses: "))
    for _ in range(n):
        print("\n--- Enter course info ---")
        cid = input("Course ID: ")
        name = input("Course name: ")

        courses.append({
            "id": cid,
            "name": name
        })


def input_marks():
    if not courses:
        print("No courses available.")
        return
    if not students:
        print("No students available.")
        return

    print("\nAvailable courses:")
    for c in courses:
        print(f"- {c['id']}: {c['name']}")

    cid = input("Enter course ID to input marks: ")

    # Check if course exists
    course_exists = any(c['id'] == cid for c in courses)
    if not course_exists:
        print("Course not found.")
        return

    marks[cid] = {}

    print(f"\nEntering marks for course: {cid}\n")
    for s in students:
        mark = float(input(f"Mark for {s['name']} (ID {s['id']}): "))
        marks[cid][s["id"]] = mark


# ---------------------------
# Listing Functions
# ---------------------------

def list_students():
    print("\n--- Student List ---")
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, DoB: {s['dob']}")


def list_courses():
    print("\n--- Course List ---")
    for c in courses:
        print(f"ID: {c['id']}, Name: {c['name']}")


def show_marks():
    if not marks:
        print("No marks available.")
        return

    cid = input("Enter course ID to show marks: ")

    if cid not in marks:
        print("No marks found for this course.")
        return

    print(f"\n--- Marks for Course {cid} ---")
    for s in students:
        sid = s["id"]
        if sid in marks[cid]:
            print(f"{s['name']} (ID {sid}): {marks[cid][sid]}")
        else:
            print(f"{s['name']} (ID {sid}): No mark")


# ---------------------------
# Main Menu
# ---------------------------

def main():
    while True:
        print("\n===== Student Mark Management =====")
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks for a course")
        print("4. List students")
        print("5. List courses")
        print("6. Show marks for a course")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            input_students()
        elif choice == "2":
            input_courses()
        elif choice == "3":
            input_marks()
        elif choice == "4":
            list_students()
        elif choice == "5":
            list_courses()
        elif choice == "6":
            show_marks()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
