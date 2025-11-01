class Person:
    #init method or constructor
    def __init__(self, name):
        self.name = name
    #sample method
    def invite(self):
        print("welcome:", self.name)
#object creation and initialization
p1 = Person('Ram')
p2 = Person('Ravi')

#method calling
p1.invite()
p2.invite()
