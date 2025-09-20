class Student:
    def __init__(self, name, grade, department):
        # Initialize attributes
        self.name = name
        self.grade = grade
        self.department = department

    def print_info(self):
        # Print student details
        print(f"Name: {self.name}")
        print(f"Grade: {self.grade}")
        print(f"Department: {self.department}")
        print("-" * 30)

    def update_grade(self, new_grade):
        # Update the grade
        self.grade = new_grade


if __name__ == "__main__":
    # Create student objects
    student1 = Student("Alice", "A", "Computer Science")
    student2 = Student("Bob", "B", "Mechanical Engineering")
    student3 = Student("Charlie", "C", "Mathematics")

    # Store multiple students in a list
    students = [student1, student2, student3]

    print("Initial Student Records:")
    for student in students:
        student.print_info()

    # Update grade of one student
    print("Updating Bob's grade to A+ ...\n")
    student2.update_grade("A+")

    # Print updated student details
    print("Updated Student Records:")
    for student in students:
        student.print_info()
