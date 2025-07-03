"""
Inheritance is a fundamental concept in OOPS that allows a class to inherit attributes and methods from another class.
"""
class Car:
    def __init__(self,windows,doors,enginetype):
        self.windows=windows
        self.doors=doors
        self.enginetype=enginetype

    def drive(self):
        print(f"the person will drive the {self.enginetype} car")


car1=Car(4,5,"petrol")
# print(car1.drive())


class Tesla(Car):
    def __init__(self, windows, doors, enginetype,is_selfdriving):
        super().__init__(windows,doors,enginetype)
        self.is_selfdriving=is_selfdriving

    def selfdriving(self):
        print(f"tesla support {self.is_selfdriving}")

tesl1=Tesla(4,5,"electic",True)
print(tesl1.selfdriving)
print(tesl1.drive())

# mutiple inheritance
class Animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        print("subclass must implement this method")

class Pet:
    def __init__(self,owner):
        self.owner=owner

class Dog(Animal,Pet):
    def __init__(self, name,owner):
        Animal.__init__(self,name)
        Pet.__init__(self,owner)
    def speak(self):
        return f"{self.name} say woof"
    
dog=Dog("Gem","Amit")
print(dog.speak())
