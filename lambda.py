def square(x):
    return x*x

def applyonlist(l1,func):
    l2=[]
    for i in l1:
        l2.append(func(i))
    return l2

print(applyonlist([1,2,3,4,5],square))

# lambda function come into picture
sqlambda=lambda x:x*x
print(sqlambda(5))

sumlabda=lambda a,b:a+b
print(sumlabda(3,5))