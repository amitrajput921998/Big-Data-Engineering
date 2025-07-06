"""
Poly-mutiple/many
morph-shape/form
"""
# In simpel words polymorphism is when a sigle entry can take mutipleform
# Method overriding
# Method overloading
# Operator Overloading

def sum(a,b):
    print(a+b)

# print(sum(2,3))

class User:
    def __init__(self,name,mobilNumber,address=""):
        if(address==""):
            self.c1(name,mobilNumber)
        else:
            self.c2(name,mobilNumber,address)

    def c2(self,name,mobilNumber):
        self.name=name
        self.mobilNumber=mobilNumber
        
    def c2(self,name,mobilNumber,address):
        self.name=name
        self.mobilNumber=mobilNumber
        self.address=address
u1=User("amit","999999","Delhi")
# print(u1)

# Method Overriding
class Animal:
    def sound(self):
        return 'Some Sound'
class Dog(Animal):
    def sound(self):
        return 'Bark'
obj=Dog()
# print(obj.sound())

