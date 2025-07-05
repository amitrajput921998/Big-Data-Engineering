"""
Procedural programming
functional programming 
and why oops is used 
"""
# class is a self define datatype

#class have two things
#1 data/attributes/property
#2 behavior/method

# class SYntax
class Car:
    pass

# Object
# An object is an instance of our class.

def sum(a,b):
    pass
print(type(sum))

# eveything in python is an object

#object literal 
swift=Car()
# print(type(swift))

# def hello():
#     print("hello python")

# print(hello("amit"))

# self is the refrence to the object created of our class.
class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def study(self):
        print(f"I am studing {self.name}")
    
s1=Student('amit',1,44)
print(s1.marks)
print(s1.study())
        

























# c1=complex()
# print(c1.real)
# print(c1.imag)