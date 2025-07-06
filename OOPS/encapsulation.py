class Student:
    noofstudent=0
    def __init__(self,name,rollno,marks):
        self.rollno=rollno
        self.name=name
        self.__marks=marks
        self.noofstudent=Student.noofstudent+1
        Student.noofstudent=Student.noofstudent+1
    # getter
    def getMarks(self):
        return self.__marks
    # setter
    def setMarks(self,newMarks):
        self.__marks=newMarks

    def study(self):
        print(f" I am {str(self.rollno)} and I am studing")
    def play(self):
        print("Padh liya, now goign to play")

s1=Student("amit",1,55)
s2=Student("mit",2,44)
# print(s1.study())
# print(s1.noofstudent)
print(s2.getMarks())
s2.setMarks(33)
print(s2.getMarks())