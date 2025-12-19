import tkinter as tk
from tkinter import simpledialog, messagebox

from domains.student import Student
from domains.course import Course
from domains.mark import Mark
from persistence import save_data, load_data


students, courses, marks = load_data()

root = tk.Tk()
root.title("PW9 - Student Management System")
root.geometry("400x400")


def add_student():
    sid = simpledialog.askstring("Student", "Student ID:")
    name = simpledialog.askstring("Student", "Student Name:")
    dob = simpledialog.askstring("Student", "Date of Birth:")
    if sid and name and dob:
        students.append(Student(sid, name, dob))
        messagebox.showinfo("OK", "Student added")


def add_course():
    cid = simpledialog.askstring("Course", "Course ID:")
    name = simpledialog.askstring("Course", "Course Name:")
    if cid and name:
        courses.append(Course(cid, name))
        messagebox.showinfo("OK", "Course added")


def add_mark():
    cid = simpledialog.askstring("Mark", "Course ID:")
    for s in students:
        m = simpledialog.askfloat("Mark", f"Mark for {s.get_id()}:")
        if m is not None:
            marks.append(Mark(cid, s.get_id(), m))
    messagebox.showinfo("OK", "Marks added")


def list_students():
    text = ""
    for s in students:
        text += f"{s.get_id()} - {s.get_name()} - {s.get_dob()}\n"
    messagebox.showinfo("Students", text if text else "No students")


def list_courses():
    text = ""
    for c in courses:
        text += f"{c.get_id()} - {c.get_name()}\n"
    messagebox.showinfo("Courses", text if text else "No courses")


def show_marks():
    cid = simpledialog.askstring("Marks", "Course ID:")
    text = ""
    for m in marks:
        if m.course_id == cid:
            text += f"{m.student_id}: {m.mark}\n"
    messagebox.showinfo("Marks", text if text else "No marks")


def on_exit():
    messagebox.showinfo("Exit", "Saving data in background...")
    t = save_data(students, courses, marks)
    root.destroy()


tk.Button(root, text="Add Student", width=30, command=add_student).pack(pady=5)
tk.Button(root, text="Add Course", width=30, command=add_course).pack(pady=5)
tk.Button(root, text="Add Mark", width=30, command=add_mark).pack(pady=5)
tk.Button(root, text="List Students", width=30, command=list_students).pack(pady=5)
tk.Button(root, text="List Courses", width=30, command=list_courses).pack(pady=5)
tk.Button(root, text="Show Marks", width=30, command=show_marks).pack(pady=5)
tk.Button(root, text="Exit", width=30, command=on_exit).pack(pady=10)

root.mainloop()
