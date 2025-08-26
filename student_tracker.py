import sqlite3

class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.grades = {}

    def add_grade(self, subject, grade):
        if 0 <= grade <= 100:
            self.grades[subject] = grade
        else:
            print("Grade must be between 0 and 100.")

    def average(self):
        if self.grades:
            return sum(self.grades.values()) / len(self.grades)
        return 0.0

    def __str__(self):
        return f"Roll: {self.roll_number}, Name: {self.name}, Grades: {self.grades}, Avg: {self.average():.2f}"


class StudentTracker:
    def __init__(self, db_name="students.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.create_tables()

    def create_tables(self):
        cur = self.conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS students (roll INTEGER PRIMARY KEY, name TEXT)")
        cur.execute("CREATE TABLE IF NOT EXISTS grades (roll INTEGER, subject TEXT, grade INTEGER)")
        self.conn.commit()

    def add_student(self, name, roll):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO students VALUES (?, ?)", (roll, name))
        self.conn.commit()

    def add_grade(self, roll, subject, grade):
        if 0 <= grade <= 100:
            cur = self.conn.cursor()
            cur.execute("INSERT INTO grades VALUES (?, ?, ?)", (roll, subject, grade))
            self.conn.commit()
        else:
            print("Invalid grade")

    def view_student(self, roll):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM students WHERE roll=?", (roll,))
        student = cur.fetchone()
        if not student:
            return None
        cur.execute("SELECT subject, grade FROM grades WHERE roll=?", (roll,))
        grades = cur.fetchall()
        return {"roll": student[0], "name": student[1], "grades": dict(grades)}

    def student_average(self, roll):
        cur = self.conn.cursor()
        cur.execute("SELECT grade FROM grades WHERE roll=?", (roll,))
        grades = [g[0] for g in cur.fetchall()]
        return sum(grades) / len(grades) if grades else 0.0
