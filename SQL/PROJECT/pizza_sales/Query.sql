create database pizzahut;
use pizzahut;

-- Q1 Retrieve the total number of order palced

SELECT 
    COUNT(order_id) AS total_order
FROM
    orders;

-- Q2 calculate total revenue generated from pizza sales;

SELECT 
    ROUND(SUM(od.quantity * p.price), 2) AS total_price
FROM
    order_details AS od
        JOIN
    pizzas AS p ON od.pizza_id = p.pizza_id;

-- Q3 Identify the highest price of pizza

SELECT 
    pt.name, p.price
FROM
    pizza_types AS pt
        JOIN
    pizzas AS p ON pt.pizza_type_id = p.pizza_type_id
ORDER BY p.price DESC
LIMIT 1;

-- Q4 Identify most common pizza size ordered

SELECT 
    p.size, COUNT(od.order_details_id) AS order_count
FROM
    pizzas AS p
        JOIN
    order_details AS od ON p.pizza_id = od.pizza_id
GROUP BY p.size
ORDER BY order_count DESC
LIMIT 1;

-- Q5 list top most ordered pizza type along with their Quantity

SELECT 
    pt.name as pizza_type, SUM(od.quantity) AS total_quantity
FROM
    pizza_types AS pt
        JOIN
    pizzas AS p ON pt.pizza_type_id = p.pizza_type_id
        JOIN
    order_details AS od ON od.pizza_id = p.pizza_id
GROUP BY pizza_type
ORDER BY total_quantity DESC
LIMIT 5;

-- Q6 join the neccessary table to find the total quantity of each pizza category orderd.

select pt.category,sum(od.quantity) as total_quantity
FROM
    pizza_types AS pt
        JOIN
    pizzas AS p ON pt.pizza_type_id = p.pizza_type_id
        JOIN
    order_details AS od ON od.pizza_id = p.pizza_id
GROUP BY pt.category
ORDER BY total_quantity DESC;

-- Q7 Determine the distrubution of orders by hour of the day

SELECT 
    HOUR(order_time) AS hour, COUNT(order_id) AS order_count
FROM
    orders
GROUP BY HOUR(order_time);