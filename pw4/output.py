def list_students(students):
    print("\n----- Students -----")
    for s in students:
        print(s.show())

def list_courses(courses):
    print("\n----- Courses -----")
    for c in courses:
        print(c.show())

def show_marks(marks, cid):
    print(f"\nMarks for course {cid}:")
    for m in marks:
        if m.course_id == cid:
            print(f"Student {m.student_id}: {m.mark}")
