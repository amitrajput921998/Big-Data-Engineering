#Encapsulation
"""
Encapsulation is the concept of wraping data (variable) and methods (function)
together as asingle unit.It resticts direct access to some of the objects's components which is a means of preventing accidental interference and misuse of the data
"""
# encapsulation with getter and setter  methods
#public,protected and private variable

class Person:
    def __init__(self,name,age):
        self.name=name  #public variable
        self.age=age    #public variable

def get_name(person):
    return person.name

person=Person("Amit",23)
# print(get_name(person))

# print(dir(person))

class Person:
    def __init__(self,name,age):
        self.__name=name  #private variable
        self.__age=age    #private variable

def get_name(person):
    return person._Person__name
person=Person("Amit",23)
# print(get_name(person))


class Person:
    def __init__(self,name,age):
        self._name=name  #protected variable
        self._age=age    #protected variable

class Employee(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

employee=Employee("Amit",23)

# print(employee._name)

# encapsulation with getter and setter

class Person:
    def __init__(self,name,age):
        self.__name=name   #private access modifer or variable
        self.__age=age     #private variable
    # getter method for name
    def get_name(self):
        return self.__name
    
    # setter method for name
    def set_name(self,name):
        self.__name=name
    
    # getter method for age
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age>0:
            self.__age=age
        else:
            print("Age cannot be negative")  

person=Person("Amit",23)
#access and modify private variable using getter and setter

print(person.get_name())
print(person.get_age())

person.set_age(25)
print(person.get_age())

