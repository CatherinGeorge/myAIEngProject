#two parent class with one child class example
class Employee:
    def __init__(self, name):#create contructor & initilization
        self.name = name

class AutomationSkill:
    def writescript(self): #no variable/parameter passed here, only methos is written
        print("writing selenium script")

#child class
class AutomationTester(Employee, AutomationSkill):
    def executetests(self):
        print(f"{self.name} is executing automation tests")

#Demonstration
if __name__ == "__main__":
    #create an AutomationTester object
    tester = AutomationTester("Catherin")
#call the methods from both parent and its own method

    print(f"Tester Name: {tester.name}")
    tester.executetests()
    tester.writescript()
    