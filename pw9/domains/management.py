import math
import numpy as np

from .student import Student
from .course import Course
from .mark import Mark


class ManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def add_student(self, student: Student):
        self.students.append(student)

    def add_course(self, course: Course):
        self.courses.append(course)

    def add_mark(self, mark: Mark):
        self.marks.append(mark)

    def find_course(self, cid):
        for c in self.courses:
            if c.get_id() == cid:
                return c
        return None

    def calculate_gpa(self):
        for s in self.students:
            weighted = []
            credits = []

            for m in self.marks:
                if m.student_id == s.get_id():
                    c = self.find_course(m.course_id)
                    if c is not None:
                        weighted.append(m.mark * c.get_credit())
                        credits.append(c.get_credit())

            if credits:
                arr_w = np.array(weighted)
                arr_c = np.array(credits)
                gpa = float(arr_w.sum() / arr_c.sum())
            else:
                gpa = 0.0

            s.set_gpa(gpa)

    def sort_students_by_gpa(self):
        self.calculate_gpa()
        self.students.sort(key=lambda s: s.get_gpa(), reverse=True)

    def get_students(self):
        return self.students

    def get_courses(self):
        return self.courses

    def get_marks(self):
        return self.marks
