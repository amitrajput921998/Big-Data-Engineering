# import math 

# print(math.sqrt(18))
# print(math.pi)

from package.maths import add
# print(add(3,4))

# Standard library overview

import array
arr=array.array('i',[1,2,3,4,5])
# print(arr)

import math
# print(math.sqrt(16))

import random
# print(random.randint(1,10))
# print(random.choice(['apple','banana','cherry']))

#file and directory access
import os
# print(os.getcwd())
# print(os.mkdir('test_dir'))

folder='test_dir'
file_path=os.path.join(folder,'new_text.txt')
with open(file_path,'w') as f:
    f.write("Data inside new file in an new folder")
# print(f"file created in folder:{file_path}")


#Data Serialization
import json
data={'name':'amit','age':25}
json_str=json.dumps(data)
# print(json_str)
# print(type(json_str))

# again converting that data into dictionary
parsed_data=json.loads(json_str)
# print(parsed_data)
# print(type(parsed_data))


# csv
import csv
with open('exp.csv',mode='w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(['name','age'])
    writer.writerow(['amit',23])

# with open('exp.csv',mode='r') as file:
#     reader=csv.reader(file)
#     for row in reader:
#         print(row)

from datetime import datetime,timedelta

now=datetime.now()
# print(now)

yesterday=now-timedelta(days=1)
# print(yesterday)

#time
import time
# print(time.time())
time.sleep(2)
# print(time.time())

# regular expression
import re
pattern=r'\d+'
text='there are 123 apples'
match=re.search(pattern,text)
print(match.group())