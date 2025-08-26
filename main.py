from student_tracker import StudentTracker

tracker = StudentTracker()

def menu():
    while True:
        print("\n--- Student Performance Tracker ---")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. View Student")
        print("4. Calculate Average")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            roll = int(input("Enter roll number: "))
            tracker.add_student(name, roll)
            print("Student added.")
        elif choice == "2":
            roll = int(input("Enter roll number: "))
            subject = input("Enter subject: ")
            grade = int(input("Enter grade (0-100): "))
            tracker.add_grade(roll, subject, grade)
            print("Grade added.")
        elif choice == "3":
            roll = int(input("Enter roll number: "))
            student = tracker.view_student(roll)
            if student:
                print(student)
            else:
                print("Student not found.")
        elif choice == "4":
            roll = int(input("Enter roll number: "))
            avg = tracker.student_average(roll)
            print(f"Average: {avg:.2f}")
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()
