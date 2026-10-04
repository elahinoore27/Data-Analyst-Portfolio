
set autocommit=0;
update orders set order_status='Cenceled22' where order_id=10;
-- commit; -- save permanatly after this you can't change it
 rollback; -- you can change undo
 select *from orders;