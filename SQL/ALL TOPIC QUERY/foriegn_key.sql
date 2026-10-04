use ecom;
create table sellers(seller_id int primary key auto_increment,seller_name varchar(20) unique not null,city varchar(20));

alter table orders add column seller_id int;
select *from orders;
alter table orders add constraint fk_order_seller foreign key(seller_id) references sellers(seller_id); -- relationship of forgrien key

select *from sellers;


insert into sellers (seller_name,city) values('TechWorld2','Patna');
insert into orders(seller_id,product,quantity,price_per_unit) values(1,"Laptip",1,6500);
insert into orders(seller_id,product,quantity,price_per_unit) values(2,"Lamp",23,5400); -- seller_id must be ivalid means 
reference table must  match with seller_id with orders table 

select *from sellers;
select *from orders;
