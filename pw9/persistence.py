import os
import pickle
import zipfile
import threading

DATA_FILE = "pw8/students.pkl"
ZIP_FILE = "pw8/students.zip"


def save_data(students, courses, marks):
    def _save():
        os.makedirs("pw8", exist_ok=True)

        with open(DATA_FILE, "wb") as f:
            pickle.dump((students, courses, marks), f)

        with zipfile.ZipFile(ZIP_FILE, "w", zipfile.ZIP_DEFLATED) as z:
            z.write(DATA_FILE)

        os.remove(DATA_FILE)

        print("[INFO] Data saved & compressed successfully.")

    t = threading.Thread(target=_save, daemon=True)
    t.start()


def load_data():
    if not os.path.exists(ZIP_FILE):
        return [], [], []

    with zipfile.ZipFile(ZIP_FILE, "r") as z:
        z.extractall()

    try:
        with open(DATA_FILE, "rb") as f:
            students, courses, marks = pickle.load(f)
    except Exception:
        return [], [], []

    os.remove(DATA_FILE)

    print("[INFO] Data loaded successfully.")
    return students, courses, marks
