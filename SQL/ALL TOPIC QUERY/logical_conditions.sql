-- use ecom;


-- select *from orders where city IN ("Delhi","Mumbai","Ahmedabad"); return only these in table
-- select *from orders where city NOT IN ("Delhi","Mumbai","Ahmedabad"); skip these city return all city
-- select *from orders where price_per_unit between 80 AND 1200;
-- select *from orders where price_per_unit NOT between 80 AND 1200;
-- select *from orders where product like "Lap%";
--  select *from orders where customer_name like "A%"; match and return 
-- select *from orders where city like "%el%";

-- wildcaerd

-- select *from orders where city like "De_hi";
-- select *from orders where customer_name like "S_ra Al_";

-- combining logical condition 
-- select *from orders where product in ("Laptop","Notebook") AND city not in ("Delhi");
-- select *from orders where product in ("Laptop","Notebook") AND price_per_unit not between 80 and 1200;
-- select *from orders where city like "%Del_i%" AND product in ("Laptop");