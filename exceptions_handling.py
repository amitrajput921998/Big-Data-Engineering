#exception handing in python allows you to handle errors gracefully and take corrective actions without stopping the execution of the program. this lesson will cover the basic of exceptions,including how to use try,except,else,and finally blocks.

# try:
#     print(a=b)
# except:
#     print("the variable is not assigned")

# try:
#     print(a=b)
# except NameError as ex:
#     print(ex)

# try:
#     result=1/0
# except ZeroDivisionError as e:
#     print(e)
#     print("please eter a valid number")

# try:
#     result=1/3
# except Exception as e:
#     print(e) 
# else:
#     print("this is executed")

# try,else,finally,else

try:
    num=int(input("enter a number"))
    result=10/num
except ValueError:
    print("that not a valid number")
else:
    print(f"the result is {result}")
finally:
    print("execution complete")
            