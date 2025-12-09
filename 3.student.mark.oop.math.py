import math
import numpy as np
import curses

class Student:
    def __init__(self, sid="", name="", dob=""):
        self.__id = sid
        self.__name = name
        self.__dob = dob
        self.gpa = 0

    def input(self):
        self.__id = input("Student ID: ")
        self.__name = input("Student name: ")
        self.__dob = input("Date of birth: ")

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def show(self):
        print(f"ID: {self.__id}, Name: {self.__name}, DoB: {self.__dob}, GPA: {self.gpa:.2f}")


class Course:
    def __init__(self, cid="", name="", credit=1):
        self.__id = cid
        self.__name = name
        self.credit = credit

    def input(self):
        self.__id = input("Course ID: ")
        self.__name = input("Course name: ")
        self.credit = int(input("Course credit: "))

    def get_id(self):
        return self.__id

    def show(self):
        print(f"ID: {self.__id}, Name: {self.__name}, Credit: {self.credit}")


class Mark:
    def __init__(self, cid, sid, mark):
        self.course_id = cid
        self.student_id = sid
        self.mark = mark


class ManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def input_students(self):
        count = int(input("Number of students: "))
        for _ in range(count):
            s = Student()
            s.input()
            self.students.append(s)

    def input_courses(self):
        count = int(input("Number of courses: "))
        for _ in range(count):
            c = Course()
            c.input()
            self.courses.append(c)

    def input_marks(self):
        if not self.courses or not self.students:
            print("Please input students and courses first.")
            return
        
        print("\nAvailable courses:")
        for c in self.courses:
            c.show()

        cid = input("Enter course ID to input marks: ")
        ok = any(c.get_id() == cid for c in self.courses)
        if not ok:
            print("Course not found.")
            return

        for s in self.students:
            sid = s.get_id()
            raw = float(input(f"Enter mark for student {sid}: "))
            rounded = math.floor(raw * 10) / 10
            self.marks.append(Mark(cid, sid, rounded))

    def calculate_gpa(self):
        for s in self.students:
            smarks = []
            scredits = []
            for m in self.marks:
                if m.student_id == s.get_id():
                    for c in self.courses:
                        if c.get_id() == m.course_id:
                            smarks.append(m.mark * c.credit)
                            scredits.append(c.credit)
            
            if scredits:
                arr_marks = np.array(smarks)
                arr_credits = np.array(scredits)
                s.gpa = float(arr_marks.sum() / arr_credits.sum())
            else:
                s.gpa = 0

    def sort_by_gpa(self):
        self.calculate_gpa()
        self.students.sort(key=lambda s: s.gpa, reverse=True)

    def list_students(self):
        self.calculate_gpa()
        print("\n----- Students -----")
        for s in self.students:
            s.show()

    def list_courses(self):
        print("\n----- Courses -----")
        for c in self.courses:
            c.show()

    def show_marks(self):
        cid = input("Course ID to show marks: ")
        print(f"\nMarks for course {cid}:")
        for m in self.marks:
            if m.course_id == cid:
                print(f"Student {m.student_id}: {m.mark}")

    def run_curses(self, screen):
        curses.curs_set(0)
        while True:
            screen.clear()
            screen.addstr(1, 2, "===== Student Management System =====")
            screen.addstr(3, 4, "1. Input students")
            screen.addstr(4, 4, "2. Input courses")
            screen.addstr(5, 4, "3. Input marks")
            screen.addstr(6, 4, "4. List students")
            screen.addstr(7, 4, "5. List courses")
            screen.addstr(8, 4, "6. Show marks")
            screen.addstr(9, 4, "7. Sort students by GPA")
            screen.addstr(10, 4, "0. Exit")
            screen.addstr(12, 4, "Choose: ")

            screen.refresh()
            choice = screen.getkey()

            if choice == "1":
                curses.endwin()
                self.input_students()
            elif choice == "2":
                curses.endwin()
                self.input_courses()
            elif choice == "3":
                curses.endwin()
                self.input_marks()
            elif choice == "4":
                curses.endwin()
                self.list_students()
                input("Press ENTER to continue")
            elif choice == "5":
                curses.endwin()
                self.list_courses()
                input("Press ENTER to continue")
            elif choice == "6":
                curses.endwin()
                self.show_marks()
                input("Press ENTER to continue")
            elif choice == "7":
                self.sort_by_gpa()
                curses.endwin()
                self.list_students()
                input("Press ENTER to continue")
            elif choice == "0":
                break


if __name__ == "__main__":
    curses.wrapper(ManagementSystem().run_curses)
