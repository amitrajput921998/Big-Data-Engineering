# class Animal:
#     def sound(self):
#         return 'Some sound'
# class Dog(Animal):
#     def sound(self):
#         return 'Bark'

# obj=Dog()
# # print(obj.sound())

# # Question two
# class Grandparent:
#     def family_name(self):
#         return 'Smith'
# class Parent(Grandparent):
#     pass

# class Child(Parent):
#     def family_name(self):
#         return 'Johnson'

# obj=Child()
# # print(obj.family_name())

# # 3 Mutiple Inhertiance
# class A:
#     def show(self):
#         return 'A'
# class B:
#     def show(self):
#         return 'B'
# class C(A,B):
#     pass

# obj=C()
# # print(obj.show())

# # Question 4
# class Parent:
#     def common(self):
#         return'Parent method'
# class Child1(Parent):
#     def specific(self):
#         return 'Child1 method'
# class Child2(Parent):
#     def specific(self):
#         return 'Child2 method'
    
# obj1=Child1()
# obj2=Child2()
# # print(obj1.common())
# # print(obj2.specific())

# # Question 5
# class Base:
#     def message(self):
#         return 'Base class message'
# class A(Base):
#     def message(self):
#         return 'A class message'
# class B(Base):
#     def message(self):
#         return 'B class message'
# class C(A,B):
#     pass

# obj=C()
# # print(obj.message())

# # qus 6
# class Grandparent():
#     def __init__(self):
#         print("Grandparent Constructor")
# class Parent(Grandparent):
#     def __init__(self):
#         super().__init__()
#         print("Parent Constructor")
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print("Child Constructor")
# obj=Child()
# # print(Child())

class A:
    def show(self):
        return 'A'
class B(A):
    def show(self):
        return 'B'
class C(A):
    def show(self):
        return 'C'
class D(B,C):
    pass
obj=D()
# print(obj.show())

class A:
    def __init__(self):
        self.value='A'
class B(A):
    def __init__(self):
        super().__init__()
        self.value='B'
class C(A):
    def __init__(self):
        super().__init__()
        self.value='C'
class D(B,C):
    def __init__(self):
        super().__init__()
obj=D()
print(obj.value)
print(D.mro())