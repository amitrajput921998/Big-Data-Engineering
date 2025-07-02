'''
File handling is a crucial part of any programming language.python provides built-in functions and methods to read from and write to files, both text and binary.this lesson will cover the basics of file handling,including reading and writing text files and binary files.
'''
#reading a whole file

# with open('sample.txt','r') as file:
#     content=file.read()
#     print(content)

# read a file line by line
# with open('sample.txt','r') as file:
#     for line in file:
#         print(line.strip()) # strip removes the neline character

# writing a file 
# with open('example.txt','w') as file:
#     file.write('hello world\n')
#     file.write('this is a new line')

# with open('example.txt','a') as file:
#     file.write("append operation taking place")

# writing a list of lines to a file
# lines=['First line \n,','second line']
# with open('example.txt','a') as file:
#     file.writelines(lines)


# working with binary files
# data=b'\x00\x01\x02\x03\x04'
# with open('text.bin','wb') as file:
#     file.write(data)

# data=b'\x00\x01\x02\x03\x04'
# with open('text.bin','rb') as file:
#     content=file.read()
#     print(content)

# with open('example.txt','r') as source_file:
#     content=source_file.read()
# with open('destination.txt','w') as destination_file:
#     destination_file.write(content)

# writing and reading the file

# with open('example.txt','w+') as file:
#     file.write("hello world\n")
#     file.write("this is a new line \n")

#     file.seek(0)

#     content=file.read()
#     print(content)
import os 
items=os.listdir('.')
# print(items)

# joing path
dir_name='folder'
file_name='file.txt'
full_path=os.path.join(os.getcwd(),dir_name,file_name)
# print(full_path)

path='example1.txt'
if os.path.exists(path):
    print(f"the path '{path}' exists")
else:
    print(f"the path '{path} does not exist")