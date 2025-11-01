class Employee:
    def __init__(self, name, employeedID):
        self.name=name
        self.employeedID=employeedID
    
class Tester(Employee):
    def __init__(self, name, employeedID):
        super().__init__(name, employeedID)

    def runTests(self):
        print(f"{self.name}/{self.employeedID} is running automation tests")

p1 = Tester("Catherin", "E3")
p1.runTests()
