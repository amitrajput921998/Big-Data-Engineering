#map function
"""
The map function applies a given function to all items in an input list and returns a map object.this is particulary useful for transforming data in a list comprehensively.
"""
def square(x):
    return x*x

# print(square(4))

# map("function,iterable")
numbers=[2,3,4,5,6]
# print(list(map(square,numbers)))
# print(list(map(lambda x:x*x,numbers)))

# map mutiple iterables
numbers1=[1,2,3]
number2=[4,5,6]

added_number=list(map(lambda x,y:x+y,numbers1,number2))
# print(added_number)

# map() to convert a list of string to integers

str_numbers=['1','2','3','4','5']
int_number=list(map(int,str_numbers))
# print(int_number)

words=['app','show','hi']

upper_word=list(map(str.upper,words))
# print(upper_word)

def get_name(person):
    return person['name']

people=[
    {'name':'amit','age':12},
    {'name':'mit','age':23},
     
]

print(list(map(get_name,people)))