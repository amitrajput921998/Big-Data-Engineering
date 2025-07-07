import sqlite3

# connect to sqllite
connection=sqlite3.connect('example.db')
print(connection)

cursor=connection.cursor()
# cursor.execute("""
# Create Table  employees(
#              id Integer Primary Key,
#              name Text Not Null,
#              age Integer,
#              department text
#                  )
# """)

# cursor.execute("""
# Insert into employees(name,age,department)
#                values ('amit',23,'data science')
# """)

# cursor.execute('select * from employees')
# rows=cursor.fetchall()

# for row in rows:
#     print(row)

# update the data in the table
# cursor.execute('''
# update employees 
#                Set age=55
#                where name='amit'
               
#                ''')

# commit the chnages
print(connection.commit())