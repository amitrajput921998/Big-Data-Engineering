# # distionary

# student={"name":"amit","age":23,"address":"india"}  # key should be unique
# print(student)

# print(student['address'])
# print(student.get('address'))

# # dictionary are nutable so you can add,update or delete elements
# student["age"]=18
# student["city"]='jaipur'
# print(student)

# student={"name":"amit","age":23,"address":"india"} 

# keys=student.keys()
# print(keys)
# print(student.values())
# print(student.items())

# # deep copy
# student_copy=student
# print(student)
# print(student_copy)

# student["name"]="sumit"
# print(student_copy)

#shallow copy
# stud=student.copy()

# student["age"]=33
# stud["age"]=12
# print(student)
# print(stud)


student={"name":"amit","age":23,"address":"india"}

#itertating over dictionaries

# for i,k in student.items():
#     print(i,k)

#dictionaries comphrehsion
square={x:x**2 for x in range(5)}
# print(square)

number=[1,2,3,3,3,4,4]
freq={}

for num in number:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
# print(freq)

dict1={"a":1,"b":2}
dict2={"b":3,"c":4}

merged_dict={**dict1,**dict2}
print(merged_dict)