from flask import Flask, request, render_template
from student_tracker import StudentTracker

app = Flask(__name__)
tracker = StudentTracker()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_student", methods=["POST"])
def add_student():
    name = request.form["name"]
    roll = int(request.form["roll"])
    tracker.add_student(name, roll)
    return f"✅ Student {name} (Roll {roll}) added!"

@app.route("/add_grade", methods=["POST"])
def add_grade():
    roll = int(request.form["roll"])
    subjects = request.form.getlist("subject")
    grades = request.form.getlist("grade")

    for subject, grade in zip(subjects, grades):
        tracker.add_grade(roll, subject, int(grade))

    return f"✅ {len(subjects)} grade(s) added for Roll {roll}!"



@app.route("/view", methods=["POST"])
def view():
    roll = int(request.form["roll"])
    student = tracker.view_student(roll)
    if not student:
        return "❌ Student not found"
    return render_template("view.html", student=student)

@app.route("/average", methods=["POST"])
def average():
    roll = int(request.form["roll"])
    student = tracker.view_student(roll)
    if not student:
        return "❌ Student not found"

    avg = tracker.student_average(roll)
    return render_template("average.html", student=student, avg=avg)

if __name__ == "__main__":
    app.run(debug=True)
