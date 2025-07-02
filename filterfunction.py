# filter function contructs an iterator from element of an iterable for which a function return true.it is used to filter out items from a list based on a condition

def even(num):
    if num%2==0:
        return True
    
# print(even(24))

l=[1,2,3,4,5,3,44,33,22]

# print(list(filter(even,l)))

number=[22,333,44,5,2,1,2222]

greater_than_five=list(filter(lambda x:x>5,number))
# print(greater_than_five)

# filter with mutiple condition
even_and_greter_then_five=list(filter(lambda x:x>5 and x%2==0,number))
print(even_and_greter_then_five)