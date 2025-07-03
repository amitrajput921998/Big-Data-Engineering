"""
Abstraction is the concept of hiding the complex implementation details and showing only the necessary features of an object. this help in reducing programming complexity and effort.
"""

from abc import ABC,abstractmethod

#abstract base class
class Vehicle(ABC):
    def drive(self):
        print("the vechicle is used for driving")

    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car enginer Started")
def operate_vechicle(vechicle):
    vechicle.start_engine()

car=Car()
print(operate_vechicle(car))