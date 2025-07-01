# # t=(1,2,3,4)
# # print(t)
# # print(type(t))

# # lst=list()
# # tpl=tuple()
# # print(type(lst))
# # print(type(tpl))

# # num=tuple([1,2,3,4,5])
# # print(type(num))

# # l=list((1,2,3,4,5))
# # print(l)
# # print(type(l))

# mixed_tuple=(1,"hello",3.14,True)
# # t=(1,2,3,4)
# # print(mixed_tuple)
# # print(mixed_tuple[1:3])
# # print(mixed_tuple[::-1])

# # r=t+mixed_tuple
# # print(r*3)

# # print(mixed_tuple.count(1))
# # print(mixed_tuple.index(1))

# packed=1,"hello",2.22
# print(packed)

# # unpacking
# a,b,c=packed
# print(a,b,c)

# # unpacking with *
# number=(1,2,3,4,5,6)
# first,*middle,last=number
# print(first)
# print(middle)
# print(last)

t=(1,2,3,4,(3,4))
print(t)
print(t[4][0])