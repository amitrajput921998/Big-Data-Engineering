select * from persons

insert into persons (id,person_name,birth_date,phone)
values (1,'mit','2/2/1998','923444213')


create table customer
(id int,
person_name varchar(30),
birth_date date,
phone varchar(20)
)

insert into customer select id,person_name from persons

select * from persons

update persons
set person_name='sumit' where id=1

delete from persons where id=1

select * from Sales.Customers where score<500 or Country='USA'

select * from Sales.Customers where Score is not null

select * from Sales.Customers where score between 500 and 800

select * from Sales.Customers where Country not in  ('USA','UK')

select * from Sales.Customers where FirstName like '%a'

select * from Sales.Customers where FirstName like '__s%'

select * from Sales.Customers where FirstName like '%r%'