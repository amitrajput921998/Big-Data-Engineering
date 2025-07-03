"""
Polymorphism is a core concept in OOPS that allows objects of diffrent classes to be treated as objects of a common superclass. It provides a way to perfrom a single action in diffrent forms. Polymorphism is typically achived through method overriding and interfaces.
"""
#Method Overriding
# method overriding allows a child class to provide a specific implementation of a methid that is already defined in it's parent class

class Animal:
    def speak(self):
        return "Sound of the animal"
    
class Dog(Animal):
    def speak(self):
        return "Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"

# function that demonstrates ploymorphism
def animal_speak(animal):
    print(animal.speak())

dog=Dog()
cat=Cat()
# print(cat.speak())

# print(animal_speak(dog))

# Polymorphism with function and methods
#Base class
class Shape:
    def area(self):
        return "the area of the figure"
    
# derived class
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return 3.14*self.radius*self.radius

def print_area(shape):
    print(f"the area is {shape.area()}")

rectangle=Rectangle(4,5)
circle=Circle(3)
# print(print_area(rectangle))
# print(print_area(circle))

# Abstract Base Classes
"""Abstract Base Classes are used to define common methods for a group of relted objects. They can enfore that derived classes implement particular methods,promoting consistency across diffrent implementations."""


from abc import ABC,abstractmethod

#define an abstrac class
class Vechicle(ABC):
    @abstractmethod
    def start_enginee(self):
        pass

class Car(Vechicle):
    def start_enginee(self):
        return "Car enginer started"
    
class Motorcycle(Vechicle):
    def start_enginee(self):
        return "Motorcycle engineer started "
    
def start_vehicle(vehicle):
    print(vehicle.start_enginee())

#create objects of car and motorcycle
car=Car()
motorcycle=Motorcycle()

print(start_vehicle(car))