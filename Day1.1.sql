/* Task: Create a database named CompanyDB and tables Employees and Departments without any constraints */

create database companydb

use companydb

create table employees(
empid int,
first_name varchar(30),
last_name varchar(30),
email varchar(50),
hiredate date,
salary decimal(10,2)
)

INSERT INTO employees (empid, first_name, last_name, email, hiredate, salary)
VALUES
(1, 'John', 'Doe', 'john.doe@example.com', '2020-01-15', 60000.00),
(2, 'Jane', 'Smith', 'jane.smith@example.com', '2019-03-22', 75000.00),
(3, 'Alice', 'Johnson', 'alice.johnson@example.com', '2021-07-30', 50000.00),
(4, 'Bob', 'Brown', 'bob.brown@example.com', '2018-11-12', 65000.00);

select * from employees

insert into employees values (5,'Amit',null,'abc@gmail.com',null,1200000)

---when you want to retrieve recods which are having null values
select * from employees where last_name is null;


select * from employees where last_name is null or hiredate is null

--- if you want to update null values you can used update statement
update employees set last_name='Rajput' where empid=5

--update a single recode
update employees
set salary=salary+1000
where empid=1

--delete quary-remove records from a table
delete from employees where empid=1

--delete mutiple records
delete from employees where salary<60000;

--Alter table
---the alter table statment modifies the structure of an exisitng table.
--- it can add,modify,or drop columns and constraints.

--add a columns to an exisiting table
alter table employees 
ADD  city varchar(20);

alter table employees add middle_name varchar(25)

select * from employees

---modify /alter the column
alter table employees alter column city varchar(10)

--rename a column
EXEC sp_rename 'employees.middle_name', 'midlename', 'COLUMN';

----drop a column
alter table employees drop column city