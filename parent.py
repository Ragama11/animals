class parent:
    def __init__(self, fname, lname):
        self.fname= fname
        self.lname = lname

    def printName(self):
        print(self.fname, self.lname)

class student(parent):
    pass
newStudent = student("Sam", "Tomashi")

newStudent.printName()

