#base class
class Person:
    def __init__(self, name):
        self.name = name
#derived class
class Employee(Person):
    def __init__(self, name, employeeID):
        super().__init__(name)
        self.employeeID=employeeID
#Further derived class
class Manager(Employee):
    def __init__(self, name, employeeID, teamsize):
        super().__init__(name, employeeID)
        self.teamsize=teamsize

    def showDetails(self):
        print(f"Name:{self.name}, EmployeeID: {self.employeeID}, Teamsize: {self.teamsize}")

p1=Manager("Catherin", 103, 15)
p1.showDetails()

       
