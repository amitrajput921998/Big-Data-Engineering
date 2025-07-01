# if statment
age=23
if age>18:
    print("you can drive")
else:
    print("you can't drive")


age=1

if age>20:
    if age>18:
        print("all check pass")
    else:
        print("it is greater")
else:
    print("not same")

# determine a leap year
y=1900

if (y%4==0 and y%100!=0) or (y%400==0):
    print("it's a leap year")
else:
    print("it's not a leap year")