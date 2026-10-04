
alter table orders
add column deliver_patner varchar(60); if u want insert values in this column
then use update function not inser b/c of insert used to create a new row and
delete is used change values of  existing row
alter table orders
rename column city to customer_city;
alter table orders
drop column rating;
select *from orders;
