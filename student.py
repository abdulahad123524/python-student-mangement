import json
import os

from grades import calculate_grades

DATA_FILE = os.path.join(os.path.dirname(__file__), "student.json")


# Load student records
def load_student():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        print("Error: Student records could not be loaded.")
        return []


# Save student records
def save_student(students):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)

        return True

    except OSError:
        print("Error: Student records could not be saved.")
        return False


# Add student
def add_student():
    print("\n========== Add Student ==========")

    name = input("Enter a name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    age_text = input("Enter age: ").strip()

    try:
        age = int(age_text)

        if age <= 0:
            print("Age must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid age.")
        return

    marks_text = input("Enter marks (0-100): ").strip()

    try:
        marks = float(marks_text)

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return

    except ValueError:
        print("Please enter valid marks.")
        return

    students = load_student()

    student = {
        "id": max((s.get("id", 0) for s in students), default=0) + 1,
        "name": name,
        "age": age,
        "marks": marks,
        "grade": calculate_grades(marks),
    }

    students.append(student)

    if save_student(students):
        print("\nStudent added successfully!")
        print(f"Student ID: {student['id']}")
        print(f"Grade: {student['grade']}")


# View all students
def view_students():
    print("\n========== All Students ==========")

    students = load_student()

    if not students:
        print("No student records found.")
        return

    for student in students:
        print(
            f"ID: {student['id']} | "
            f"Name: {student['name']} | "
            f"Age: {student['age']} | "
            f"Marks: {student['marks']} | "
            f"Grade: {student['grade']}"
        )


# View single student
def view_student_details():
    print("\n========== Student Details ==========")

    students = load_student()

    if not students:
        print("No student records found.")
        return

    try:
        student_id = int(input("Enter student ID: "))

    except ValueError:
        print("Please enter a valid numeric ID.")
        return

    student = next((s for s in students if s["id"] == student_id), None)

    if student is None:
        print("Student not found.")
        return

    print("\n========== Student Profile ==========")
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Marks: {student['marks']}")
    print(f"Grade: {student['grade']}")


# Delete student
def delete_student():
    print("\n========== Delete Student ==========")

    students = load_student()

    if not students:
        print("No student records found.")
        return

    try:
        student_id = int(input("Enter student ID to delete: "))

    except ValueError:
        print("Please enter a valid numeric ID.")
        return

    student = next((s for s in students if s["id"] == student_id), None)

    if student is None:
        print("Student not found.")
        return

    print(f"Selected student: {student['name']}")

    confirmation = input("Are you sure you want to delete? (y/n): ").strip().lower()

    if confirmation != "y":
        print("Deletion cancelled.")
        return

    updated_students = [s for s in students if s["id"] != student_id]

    if save_student(updated_students):
        print("Student deleted successfully.")
