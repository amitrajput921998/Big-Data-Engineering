# # lst=[]
# # print(type(lst))

# # name=['hello','max',23]
# # print(name)

# fruits=['apple','bannaa','chiku']

# print(fruits[0].upper())

# fruits[1]="water"
# print(fruits)

# # list methids
# fruits.append("mango")
# print(fruits)

# l=[2,3,4,5,6,6,4,3,2]
# print(l[2:5])
# print(l[:5])
# print(l[5:])
# print(l[::2])
# # print(l[::-1])
# l=[1,2,3,4,"hello"]
# for i,l in enumerate(l):
#     print(i,l)

# list comperhension
# l=[x**2 for x in range(1,10)]
# print(l)

# even_no=[x for x in range(1,10) if x%2==0]
# print(even_no)

# ls1=[1,2,3,4]
# ls2=['a','b','c','d']

# pair=[[i,j] for i in ls1 for j in ls2]
# print(pair)

words=["hello","world","python","list","compherehension"]
length=[len(words) for words in words]
print(length)

to_do_list=["buy groies","pay bills"]

to_do_list.append("run")
to_do_list.append("gym")

to_do_list.remove("buy groies")

if "pay bills" in to_do_list:
    print("don't forogot to pay bills")
print("to do list task")
for task in to_do_list:
    print(f"{task}")