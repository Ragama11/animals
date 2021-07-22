class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def getUsername(self):
        return self.username

    def setUsername(self, username):
        self.username = username  

class Student(User):
    pass

newUser = Student("Dossy","dossysibi2@gmail.com", "gggggg")


print(newUser.getUsername())