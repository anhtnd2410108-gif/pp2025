from domains.student import Student
from domains.course import Course
from domains.mark import Mark

STUDENT_FILE = "pw5/students.txt"
COURSE_FILE = "pw5/courses.txt"
MARK_FILE = "pw5/marks.txt"

def input_students():
    lst = []
    count = int(input("Number of students: "))

    with open(STUDENT_FILE, "w", encoding="utf-8") as f:
        for _ in range(count):
            sid = input("Student ID: ")
            name = input("Student name: ")
            dob = input("Date of birth: ")

            s = Student(sid, name, dob)
            lst.append(s)

            f.write(f"{sid},{name},{dob}\n")

    return lst

def input_courses():
    lst = []
    count = int(input("Number of courses: "))

    with open(COURSE_FILE, "w", encoding="utf-8") as f:
        for _ in range(count):
            cid = input("Course ID: ")
            name = input("Course name: ")
            credit = int(input("Course credit: "))

            c = Course(cid, name, credit)
            lst.append(c)

            f.write(f"{cid},{name},{credit}\n")

    return lst

import math

def input_marks(students, courses):
    marks = []

    with open(MARK_FILE, "w", encoding="utf-8") as f:
        for c in courses:
            for s in students:
                raw = float(input(f"Mark for {s.get_id()} in {c.get_id()}: "))
                mark = math.floor(raw * 10) / 10

                m = Mark(c.get_id(), s.get_id(), mark)
                marks.append(m)

                f.write(f"{c.get_id()},{s.get_id()},{mark}\n")

    return marks
