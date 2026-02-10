import json
class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
    def to_dict(self):
        return {
            "roll": self.roll,
            "name": self.name,
            "marks": self.marks
        }
class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = []
        self.load_data()
    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                self.students = [Student(**s) for s in data]
        except FileNotFoundError:
            self.students = []
    def save_data(self):
        with open(self.filename, "w") as file:
            json.dump([s.to_dict() for s in self.students], file, indent=4)
    def add_student(self, roll, name, marks):
        for s in self.students:
            if s.roll == roll:
                print("Student already exists!")
                return
        student = Student(roll, name, marks)
        self.students.append(student)
        self.save_data()
        print("Student added successfully!")
    def view_students(self):
        if not self.students:
            print("No students found!")
            return
        print("\n--- Student List ---")
        for s in self.students:
            print(f"Roll: {s.roll} | Name: {s.name} | Marks: {s.marks}")
    def search_student(self, roll):
        for s in self.students:
            if s.roll == roll:
                print(f"Found: {s.name} - {s.marks} marks")
                return
        print("Student not found!")
    def delete_student(self, roll):
        for s in self.students:
            if s.roll == roll:
                self.students.remove(s)
                self.save_data()
                print("Student deleted!")
                return
        print("Student not found!")
def main():
    manager = StudentManager()
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            roll = input("Roll No: ")
            name = input("Name: ")
            marks = int(input("Marks: "))
            manager.add_student(roll, name, marks)
        elif choice == "2":
            manager.view_students()
        elif choice == "3":
            roll = input("Enter Roll No: ")
            manager.search_student(roll)
        elif choice == "4":
            roll = input("Enter Roll No: ")
            manager.delete_student(roll)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()

