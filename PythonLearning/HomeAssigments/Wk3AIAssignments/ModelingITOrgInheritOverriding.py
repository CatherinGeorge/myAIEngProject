# Base class
class Employee:
    def __init__(self, name, emp_id, department):
        self.name = name
        self.emp_id = emp_id
        self.department = department

    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Department: {self.department}")


# Subclass: Manager
class Manager(Employee):
    def __init__(self, name, emp_id, department, team_size):
        super().__init__(name, emp_id, department)  # Call parent constructor
        self.team_size = team_size

    def display_info(self):
        super().display_info()  # Reuse parent details
        print(f"Team Size: {self.team_size}")


# Subclass: Developer
class Developer(Employee):
    def __init__(self, name, emp_id, department, programming_language):
        super().__init__(name, emp_id, department)  # Call parent constructor
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()  # Reuse parent details
        print(f"Programming Language: {self.programming_language}")


if __name__ == "__main__":
    # Create Manager object
    manager = Manager("Alice Johnson", "M001", "IT Operations", 12)

    # Create Developer object
    developer = Developer("Bob Smith", "D101", "Software Development", "Python")

    print("=== Manager Details ===")
    manager.display_info()

    print("\n=== Developer Details ===")
    developer.display_info()
