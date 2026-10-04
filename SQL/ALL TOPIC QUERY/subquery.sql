use ecom;
-- select city,count(*) as total_orders from orders group by city;
-- select category,count(*) as total_orders from orders group by category;
-- select city,count(*) as total_orders,sum(quantity*price_per_unit) as total_sales from orders group by city;
-- select category,count(*) as total_orders,sum(quantity*price_per_unit) as total_sales from orders group by category;
-- select city,count(*) as total_orders,avg(price_per_unit) as avgrage_sales from orders group by city;
-- select city,order_status ,count(*) as count from orders group by city,order_status;

-- select city,order_status ,count(*) as count from orders group by city,order_status having city in ('Delhi','Pune','Surat');
-- fitlter using having having 

-- select city,order_status ,count(*) as count from orders group by city,order_status order by count ;
-- select city,order_status ,count(*) as count from orders group by city,order_status order by count desc;


