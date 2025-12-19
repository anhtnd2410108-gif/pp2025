import pickle
import zipfile
import os

DATA_FILE = "pw6/students.pkl"
ZIP_FILE = "pw6/students.dat"


def save_data(students, courses, marks):
    with open(DATA_FILE, "wb") as f:
        pickle.dump((students, courses, marks), f)

    with zipfile.ZipFile(ZIP_FILE, "w") as z:
        z.write(DATA_FILE)

    os.remove(DATA_FILE)


def load_data():
    if not os.path.exists(ZIP_FILE):
        return [], [], []

    with zipfile.ZipFile(ZIP_FILE, "r") as z:
        z.extractall("pw6")

    with open(DATA_FILE, "rb") as f:
        students, courses, marks = pickle.load(f)

    os.remove(DATA_FILE)
    return students, courses, marks
