use ecom;
 alter  table orders
 DROP foreign key fk_order_seller; it one 

 alter table orders
 add constraint fk_order_seller
 foreign key(seller_id)
 references sellers(seller_id)
 on delete cascade; -- it's all link or relationship data from  table


 delete from sellers 
 where seller_id =2;
 select *from orders;

 select *from sellers;

 alter  table orders
 DROP foreign key fk_order_seller; it one 

alter table orders
 add constraint fk_order_seller
 foreign key(seller_id)
 references sellers(seller_id)
 on delete set null; -- 
 delete from orders
 where id =2; it is only delete id not all data all data same as it is



