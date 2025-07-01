# # # s={1,2,3,4,5,1,2,3,4}
# # # print(s)

# # # # adding and removing elementset

# # # s.add(7)
# # # print(s)

# # # # removing the element
# # # # s.remove(12)
# # # # print(s)

# myset={"apple","banana","cherry","apple",True,1}

# # # print(myset)
# # # print(len(myset))

# # # for x in myset:
# # #     print(x)

# # # print("appl" in myset)
# # topical={"tree","flower","rose"}

# # myset.add("chickue")
# # # print(myset)

# # myset.update(topical)
# # # print(myset)

# # myset.remove("rose") # if the irems are not there remove will raise error
# # # print(myset)

# # myset.discard("amit")
# # print(myset)

# set1={"a","b","c"}
# set2={1,2,3}
# # set3=set1.union(set2)
# # print(set3)

# set3=set1|set2
# print(set3)

my_set={1,2,3,4,5,6}

my_set.add(22)
# my_set.remove(222)
# my_set.discard(22)
# my_set.pop()
# print(2 in my_set)
# print( my_set)

set1={1,2,3,4,5}
set2={4,5,6,6,7,8}
# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.intersection_update(set2))
# print(set1.difference(set2))

# symetic diff
# print(set1.symmetric_difference(set2))

# set1={1,2,3}
# set2={1,2,3,3,4,5}

# print(set1.issubset(set2))
# print(set1.issuperset(set2))

text="hello how are you i am good hello i am also good"
words=text.split()
final_unique_words=set(words)
print(final_unique_words)