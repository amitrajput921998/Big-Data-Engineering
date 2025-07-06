"""
Fundamental concept of oops that involve hiding complex implementation details and showing only essential features

# We have to ensure 2 things
from abc import ABC,abstractmethod
1. Inherit abc class
2. Should have an abstract method
"""
from abc import ABC, abstractmethod
class User(ABC):
    @abstractmethod
    def login(self):
        pass
    def logout(self):
        print("logout")
    @abstractmethod
    def auth(self):
        pass

class Buyer(User):
    def login(self):
        if(self.auth):
            print("logging in user")
    def checkObject(self,link):
        print(link)
    def auth(self):
        pass


b1=Buyer()
print(b1.auth())