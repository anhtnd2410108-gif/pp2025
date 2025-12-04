# OOP

class Student:
    def __init__(self, sid="", name="", dob=""):
        self.__id = sid
        self.__name = name
        self.__dob = dob

    def input(self):
        self.__id = input("Student ID: ")
        self.__name = input("Student name: ")
        self.__dob = input("Student date of birth: ")

    def get_id(self):
        return self.__id

    def show(self):
        print(f"ID: {self.__id}, Name: {self.__name}, DoB: {self.__dob}")


class Course:
    def __init__(self, cid="", name=""):
        self.__id = cid
        self.__name = name

    def input(self):
        self.__id = input("Course ID: ")
        self.__name = input("Course name: ")

    def get_id(self):
        return self.__id

    def show(self):
        print(f"ID: {self.__id}, Name: {self.__name}")


class Mark:
    def __init__(self, course_id, student_id, mark):
        self.course_id = course_id
        self.student_id = student_id
        self.mark = mark


class ManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []  # list of Mark objects

        # Input section
 

    def input_students(self):
        count = int(input("Number of students: "))
        for _ in range(count):
            print("---- Input student ----")
            s = Student()
            s.input()
            self.students.append(s)

    def input_courses(self):
        count = int(input("Number of courses: "))
        for _ in range(count):
            print("---- Input course ----")
            c = Course()
            c.input()
            self.courses.append(c)

    def input_marks(self):
        if not self.courses or not self.students:
            print("Please input courses and students first.")
            return

        print("\nAvailable courses:")
        for c in self.courses:
            c.show()

        cid = input("Enter course ID to input marks: ")

        # Verify course exists
        if not any(c.get_id() == cid for c in self.courses):
            print("Course not found.")
            return

        for s in self.students:
            sid = s.get_id()
            mark = float(input(f"Mark for student {sid}: "))
            self.marks.append(Mark(cid, sid, mark))

   
    # Listing section
    

    def list_students(self):
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

    
    # Main loop
   

    def run(self):
        while True:
            print("\n===== OOP Student Mark Management =====")
            print("1. Input students")
            print("2. Input courses")
            print("3. Input marks")
            print("4. List students")
            print("5. List courses")
            print("6. Show marks")
            print("0. Exit")

            choice = input("Choose: ")

            if choice == "1":
                self.input_students()
            elif choice == "2":
                self.input_courses()
            elif choice == "3":
                self.input_marks()
            elif choice == "4":
                self.list_students()
            elif choice == "5":
                self.list_courses()
            elif choice == "6":
                self.show_marks()
            elif choice == "0":
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    app = ManagementSystem()
    app.run()
