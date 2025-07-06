class Student:
    noofstudent=0
    def __init__(self,name,rollno,marks):
        self.rollno=rollno
        self.name=name
        self.marks=marks
        self.noofstudent=Student.noofstudent+1
        Student.noofstudent=Student.noofstudent+1

    def study(self):
        print(f" I am {str(self.rollno)} and I am studing")
    def play(self):
        print("Padh liya, now goign to play")

s1=Student("amit",1,55)
s1=Student("mit",2,44)
print(s1.study())
print(s1.noofstudent)