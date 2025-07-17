def applyonelist(l1,func):
    l2=[]
    for i in l1:
        l2.append(func(i))
    return l2

def squ(x):
    return x*x
l=list(map(squ,[1,2,3,4,5]))
# print(l)


# filter function
def iseven(num):
    return num%2==0

f1=list(filter(iseven,[1,2,3,4,5]))
print(f1)

# reduce
from functools import reduce
l1=reduce(lambda a,b:a*b,[1,2,3,4])
print(l1)