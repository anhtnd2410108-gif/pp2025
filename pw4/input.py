from domains.student import Student
from domains.course import Course
from domains.mark import Mark

def input_students():
    lst = []
    count = int(input("Number of students: "))
    for _ in range(count):
        sid = input("Student ID: ")
        name = input("Student name: ")
        dob = input("Date of birth: ")
        lst.append(Student(sid, name, dob))
    return lst

def input_courses():
    lst = []
    count = int(input("Number of courses: "))
    for _ in range(count):
        cid = input("Course ID: ")
        name = input("Course name: ")
        lst.append(Course(cid, name))
    return lst

def input_marks(students, courses):
    marks = []
    cid = input("Course ID to input marks: ")

    for s in students:
        m = float(input(f"Mark for {s.id}: "))
        marks.append(Mark(cid, s.id, m))
    return marks
