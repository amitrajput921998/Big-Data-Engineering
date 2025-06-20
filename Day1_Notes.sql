---#create databse schooldb,student(studentid,firstname,lastname,email,enrollment date)
create database schooldb

--createing table student
use schooldb
create table student(
studentid int,
firstname varchar(30),
lastname varchar(30),
email varchar(30),
enrollment_date date
)
---create course table (courseid,coursename,department)

create table course(
courseid int,
coursename varchar(30),
department varchar(30),
credits int
)

insert into student values (1,'Amit','Singh','abc@gmail.com', '8-8-2021')
insert into student values (2,'Jay','Modi','dec@gmail.com', '9-8-2021')
insert into student values (3,'Mit','Rajput','ers@gmail.com', '2-8-2023')
insert into student values (4,'Sumit','Mehta','wsa@gmail.com', '3-2-2020')
insert into student values (5,'Pravin','Yadav','kiu@gmail.com', '5-9-2022')

select * from student

select * from course

insert into course values (1,'Computer Network','CSE',5)
insert into course values (2,'EC','EEC',4)

drop table course

drop table student

drop database schooldb