USE demo;
select count(*) from orders;
select sum(quantity*price_per_unit) as total_revenue from orders;
select avg(price_per_unit) from orders;
select avg(price_per_unit) as Avg_order from orders;
select min(price_per_unit) as Min_price, max(price_per_unit)  as Max_price from orders;
select round(price_per_unit,0) as Round_price from orders;
select lower(customer_city) as lower_city, upper(customer_name) as customer_upper_name from orders;
select customer_name , length(customer_name) as name_length from orders ;
SELECT customer_name,
       LENGTH(customer_name) AS name_length
FROM orders
WHERE customer_name = 'Amit Sharma';
select current_date();
select current_time();
select order_id, datediff(delivery_date,order_date) as delivery_day from orders
select order_id, datediff(delivery_date,order_date) as delivery_day from orders where customer_name="Amit Sharma";
select *from orders
where year(order_date)=2025;
select *from orders
where year(order_date)=2026;
