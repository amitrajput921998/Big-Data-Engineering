class User:
    def __init__(self,name,id,age,passCode):
        self.name=name
        self.id=id
        self.age=age
        self.passCode=passCode
    def login(self):
        print(" P logged in")
    def _logout(self):
        print(" P logged out")

class Student(User):
    def __init__(self,marks,rollno, name, id, age, passCode):
        super().__init__(name, id, age, passCode)
        self.marks=marks
        self.rollno=rollno

    def login(self):
        print("OTP sent")
        print("Student Loggin in")

s1=Student(90,123,"amit",1,25,"0000")
print(s1.login())