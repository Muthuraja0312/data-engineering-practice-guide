38. Find Customers Who Are Not Blacklisted
Question:
Write a SQL query to find all orders belonging to customers who are not blacklisted.
Orders Table
order_id	customer_id
1	10
2	20
3	NULL
Blacklisted_Customers Table
customer_id
10
NULL
Expected result:
order_id	customer_id
2	20
3	NULL

select o.order_id,o.customer_id from orders o where not exists (select customer_id from blacklisted_customers b where b.customer_id = o.customer_id)
