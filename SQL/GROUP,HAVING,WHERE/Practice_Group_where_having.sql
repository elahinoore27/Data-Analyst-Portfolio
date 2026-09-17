use def_function;

-- CREATE TABLE sales_orders (
--     order_id INT PRIMARY KEY,
--     product_category VARCHAR(50),
--     city VARCHAR(50),
--     quantity INT,
--     amount DECIMAL(10,2)
-- );

-- INSERT INTO sales_orders (order_id, product_category, city, quantity, amount)
-- VALUES
-- (1, 'Electronics', 'Delhi', 2, 50000),
-- (2, 'Clothing', 'Mumbai', 5, 7500),
-- (3, 'Electronics', 'Delhi', 1, 30000),
-- (4, 'Grocery', 'Mumbai', 10, 4000),
-- (5, 'Clothing', 'Delhi', 3, 4500),
-- (6, 'Grocery', 'Delhi', 8, 3200),
-- (7, 'Electronics', 'Mumbai', 2, 60000),
-- (8, 'Clothing', 'Mumbai', 4, 6000),
-- (9, 'Grocery', 'Delhi', 6, 2400),
-- (10, 'Electronics', 'Delhi', 1, 25000);

-- select product_category,sum(amount) as total_Price from sales_orders
-- group by product_category;

-- select city ,sum(quantity) as total_quantity
-- from sales_orders
-- group by city;

-- select city ,avg(amount) as average_amont from sales_orders
-- group by city;

-- -- select product_category , max(amount) as max_Order_Amount from 
-- -- sales_orders 
-- -- group by product_category;

-- -- select city, min(quantity) as Lowest_order_quanity from
-- -- sales_orders
-- -- group by city;

-- -- 3. Product categories with more than 3 orders
-- SELECT product_category, COUNT(order_id) AS total_orders
-- FROM sales_orders
-- GROUP BY product_category
-- HAVING COUNT(order_id) > 3;

-- -- 1. Product categories with total sales greater than 20000
-- SELECT product_category, SUM(amount) AS total_sales
-- FROM sales_orders
-- GROUP BY product_category
-- HAVING SUM(amount) > 20000;

-- -- 2. Cities with total quantity sold greater than 20
-- SELECT city, SUM(quantity) AS total_quantity
-- FROM sales_orders
-- GROUP BY city
-- HAVING SUM(quantity) > 20;

-- -- 4. Cities with average order amount greater than 19000
-- SELECT city, AVG(amount) AS average_amount
-- FROM sales_orders
-- GROUP BY city
-- HAVING AVG(amount) > 19000;

-- -- 5. City and product category combinations with total sales over 10000
-- SELECT city, product_category, SUM(amount) AS total_sales
-- FROM sales_orders
-- GROUP BY city, product_category
-- HAVING SUM(amount) > 10000;

-- -- 6. Product categories where the highest order amount is greater than 50000
-- SELECT product_category, MAX(amount) AS highest_amount
-- FROM sales_orders
-- GROUP BY product_category
-- HAVING MAX(amount) > 50000;


-- -- 7. Cities where the lowest ordered quantity is greater than 1
-- SELECT city, MIN(quantity) AS lowest_quantity
-- FROM sales_orders
-- GROUP BY city
-- HAVING MIN(quantity) > 1;

-- select product_category,sum(amount) as total_sale
-- from sales_orders
-- where city='Delhi'
-- group by product_category;

-- select product_category,
-- sum(amount) as total_sale
-- from sales_orders
-- where quantity >1
-- group by product_category
-- having sum(amount)>50000;

-- 4. Total sales by city for Electronics and Clothing orders
-- SELECT city, SUM(amount) AS total_sales
-- FROM sales_orders
-- WHERE product_category IN ('Electronics', 'Clothing')
-- GROUP BY city;
-- 5. City/category groups with quantity above 5, for orders above 3000
-- SELECT city, product_category, SUM(quantity) AS total_quantity
-- FROM sales_orders
-- WHERE amount > 3000
-- GROUP BY city, product_category
-- HAVING SUM(quantity) > 5;

-- 6. Categories with more than 2 orders, only for Mumbai
-- SELECT product_category, COUNT(order_id) AS total_orders
-- FROM sales_orders
-- WHERE city = 'Mumbai'
-- GROUP BY product_category
-- HAVING COUNT(order_id) > 2;

-- 7. Cities with average amount above 10000, where quantity is at least 2
-- SELECT city, AVG(amount) AS average_amount
-- FROM sales_orders
-- WHERE quantity >= 2
-- GROUP BY city
-- HAVING AVG(amount) > 10000;
