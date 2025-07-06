import os

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def to_string(self):
        return f"{self.student_id},{self.name}\n"

    @staticmethod
    def from_string(data):
        student_id, name = data.strip().split(",")
        return Student(student_id, name)

class StudentManager:
    FILE_NAME = "students.txt"

    def add_student(self):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        student = Student(student_id, name)

        with open(self.FILE_NAME, "a") as file:
            file.write(student.to_string())
        print("✅ Student added successfully!")

    def view_students(self):
        print("\n📋 All Students:")
        if not os.path.exists(self.FILE_NAME):
            print("No student records found.")
            return

        with open(self.FILE_NAME, "r") as file:
            for line in file:
                student = Student.from_string(line)
                print(f"ID: {student.student_id} | Name: {student.name}")

    def search_student(self):
        search_id = input("Enter student ID to search: ")
        found = False

        if not os.path.exists(self.FILE_NAME):
            print("No student records found.")
            return

        with open(self.FILE_NAME, "r") as file:
            for line in file:
                student = Student.from_string(line)
                if student.student_id == search_id:
                    print(f"✅ Found: ID: {student.student_id}, Name: {student.name}")
                    found = True
                    break

        if not found:
            print("❌ Student not found.")

def main():
    manager = StudentManager()

    while True:
        print("\n=== Student Record System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.view_students()
        elif choice == "3":
            manager.search_student()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()

# This code implements a simple Student Record System that allows users to add, view, and search for student records.
# It uses a text file to store student data, ensuring that records persist between program runs.
# The system is designed to be user-friendly, providing clear prompts and feedback for each action.
# The code is structured with a `Student` class to represent individual student records
