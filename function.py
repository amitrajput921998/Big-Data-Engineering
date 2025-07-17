# def sum(a,b):
#     return a+b

# fun1=sum
# print(fun1(1,2))

# l=[1,2,3,4,5]

# l.append(sum)
# print(l)

# print(type(sum))

# # Can be passed as an argument to another function
# def sum(a,b):
#     print(a+b)

# sum(2,3)

# def squareofNumber(x):
#     return x*x

# a=squareofNumber(5)
# print(a)

# def squareofalist(l1):
#     l1square=[]
#     for i in l1:
#         l1square.append(squareofNumber(i))

#     return l1square
# l1=[2,3,4,5]
# result=squareofalist(l1)

# Write a program to get a list and return each and every element as a positive/abs value
import math

def absoluteofnumber(x):
    return math.fabs(x)

def operationonlist(l1,func):
    l1modified=[]
    for i in l1:
        l1modified.append(func(i))
    return l1modified

l1=[2,3,4,-3,-4,5]

result=operationonlist(l1,absoluteofnumber)
# print(result)

def greet(name):
    return f"Namaste {name}"

def hello():
    return greet("Amit")

# print(hello())

def factorial():
    return math.factorial

factorial()
print(factorial())

def FindFactorial(num):
    f=factorial()
    return f(num)

print(FindFactorial(5))