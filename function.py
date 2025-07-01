#  A function is a block of code that performs a specific task. Functions help in organizing code,reusing code, and improving readability
# Sytax
# def function_name(para):
#     return expression

def even_or_odd(num):
    if num%2==0:
        print("the number is even")
    else:
        print("the number is oddd")


# print(even_or_odd(22))


def add(a,b):
    return a+b

result=add(3,4)
# print(result)

# default parameters
def greet(name="max"):
    print(f"hello {name}")

# print(greet())

# variable length arguments
# postional and keywords arguments
def print_number(*args):
    for num in args:
        print(num)

# print(print_number(1,2,3,4,5,6))
    
# keywords arguments

def print_details(**kwargs):
    for k,v in kwargs.items():
        print(k,v)

print(print_details(name="max",age=23))