create table customers(
customer_id INT PRIMARY KEY auto_increment,
name varchar(100),
email VARCHAR(150),
age INT,
phone VARCHAR(12),
is_active BOOLEAN,
singup_date DATE,
created_at DATETIME,
total_spend DECIMAL(10,2)
)
DROP table customers;
