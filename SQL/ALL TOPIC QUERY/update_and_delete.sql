
-- update orders
-- set order_status="Delivered"
-- where order_id=10;
-- update orders set discount_percent=10,
-- rating=5 where order_id=1; --when in place order_id write customer_name is not safe update the 
-- you must safe mode disable to run query because of primary key always use to update use primary key
delete from orders where order_id=4;
 select *from orders;
