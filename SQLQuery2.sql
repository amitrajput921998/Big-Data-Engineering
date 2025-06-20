select * from customers
select * from orders

select * from customers c inner join orders o on c.id=o.customer_id 

select id,first_name,order_id,sales from customers c left join orders o on c.id=o.customer_id

select id,first_name,order_id,sales from customers c right join orders o on c.id=o.customer_id

select id,first_name,order_id,sales from customers c full outer join orders o on c.id=o.customer_id

---this is left anti join 
select id,first_name,order_id,sales from customers c left join orders o on c.id=o.customer_id where o.customer_id is null
--this is right anti join
select id,first_name,order_id,sales from customers c right join orders o on c.id=o.customer_id where c.id is null

select * from orders o left join customers c on o.customer_id=c.id where c.id is null 

select * from orders o full join customers c on o.customer_id=c.id where c.id is null or o.customer_id is null 

select * from customers as c left join orders as o on c.id=o.customer_id where o.customer_id is not null

--cross join

select * from customers cross join orders