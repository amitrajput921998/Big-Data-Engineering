# """
# Object-Oriented Programming(OOPS) is a programming paradigm that uses "objects" to design application and computer programs. OOPS allows for modelling real-world scenarious using classes and objects.
# """
# #  A class is a blue print for creating objects,attributes,methods
# class Car:
#     pass

# audi=Car()

# # print(type(audi))

# # instance
# class Dog:
#     # constructor
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def bark(self):
#         print(f"{self.name} says woof")
# dog1=Dog("buddy",3)
# print(dog1)
# print(dog1.name)
# print(dog1.age)
# print(dog1.bark())

class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount} is deposited. New balanced is {self.balance}")
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient funds")
        else:
            self.balance-=amount
            print(f"{amount} is withdrawn.new balance is {self.balance}")
    def get_balance(self):
        return self.balance
    
account=BankAccount("Amit",4000)
print(account)

account.deposit(3000)
print(account.get_balance)

account.withdraw(2000)
print(account.get_balance)
    