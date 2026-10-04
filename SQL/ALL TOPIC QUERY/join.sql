use ecom ;

insert into sellers values(1,"DON","DELHI");
insert into sellers values(2," MON","DELHI21");
insert into sellers values(3,"DON-NIGHT","MUMBAI");
insert into sellers values(4,"DON1-NIGHT","PUNE");
update orders set seller_id=2 where order_id in (2,3,7,8,10,11,12);
update orders set seller_id=1 where order_id in (1,4,5,6,9);
 update orders set seller_id=NULL where order_id in (1,4,5,6,9



inner join 

select o.order_id,o.product,o.city as customer_city,s.seller_name from orders o inner join sellers s on 
o.seller_id=s.seller_id;
select *from orders;
select *from sellers; 

left join left table values

 select o.order_id,o.product,o.city as customer_city,s.seller_name from orders o left join sellers s on 
o.seller_id=s.seller_id;

right join it is right table values
select o.order_id,o.product,o.city as customer_city,s.seller_name from orders o right join sellers s on 
 o.seller_id=s.seller_id;


select *from orders;
