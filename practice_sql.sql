select * from customers;
select *
from orders;

select max(o.amount),o.customer_id,c.customer_name
from orders o
join customers c
on o.customer_id = c.customer_id
group by o.customer_id, c.customer_name;


select count(DISTINCT c.customer_id)
from customers c
join orders o
on c.customer_id = o.customer_id
where c.country = 'USA';

SELECT customers.customer_name,orders.amount
from customers
join orders
on customers.customer_id = orders.customer_id
where amount > 400;


select orders.order_date,customers.customer_name
from orders
join customers
on orders.customer_id = customers.customer_id
order by order_date desc
limit 1;

select extract(month from  orders.order_date)
from orders;

SELECT to_char(orders.order_date, 'Month') as month
from orders;

SELECT sum(orders.amount)
from orders;

select avg(orders.amount),customers.customer_name
from orders
join  customers
on orders.customer_id = customers.customer_id
group by customers.customer_name ;


select count(orders.customer_id),customers.customer_name
from customers
join orders
on customers.customer_id = orders.customer_id
group by customers.customer_name
order by  count(orders.customer_id) desc ;


select count(orders.customer_id),customers.customer_name
from customers
join orders
on customers.customer_id = orders.customer_id
group by customers.customer_name
having count(orders.customer_id) = 0;

