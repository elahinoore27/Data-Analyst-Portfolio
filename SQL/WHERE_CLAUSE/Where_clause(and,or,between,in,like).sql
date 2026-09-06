USE practice;
-- create table employees(
-- id int,
-- name varchar(20),
-- age int,
-- department varchar(20),
-- salary int,
-- city varchar(20),
-- experience int
-- );

-- INSERT INTO employees VALUES
-- (1, 'Rahul', 22, 'IT', 30000, 'Pune', 1),
-- (2, 'Aman', 25, 'HR', 40000, 'Mumbai', 3),
-- (3, 'Neha', 28, 'IT', 55000, 'Pune', 5),
-- (4, 'Priya', 24, 'Sales', 35000, 'Delhi', 2),
-- (5, 'Arjun', 30, 'IT', 70000, 'Mumbai', 7),
-- (6, 'Sara', 26, 'HR', 45000, 'Pune', 4),
-- (7, 'Vikas', 32, 'Sales', 60000, 'Delhi', 8),
-- (8, 'Riya', 23, 'IT', 32000, 'Pune', 1);

-- Where Clause
-- Display all employee whose age is greater than 25

-- select *from employees
-- where age>25;

-- Display all employee whose Salary is greater than 55000

-- select *from employees
-- where salary>=55000;

-- Where And
-- Display IT employee who Live in Pune

-- select *from employees
-- where department='IT' and city='Pune';

-- Display HR employees whose age is greater than 25

-- select *from employees
-- where department='HR' and age>25;

-- Where OR

-- Display  employees who are from pune or mumbai 
-- select *from employees
-- where city='Pune' or city= 'Mumbai';

-- Display employee in working in IT Or HR

-- select *from employees
-- where department='HR' or department='IT';

-- where Between

-- Find employees whose age between 25 and 30

-- select *from employees
-- where age between 25 and 30;
-- Find employees whose experience between 3 and 4

-- select *from employees
-- where experience between 3 and 4

-- Where IN

-- Find employees whose live Pune or Mumbai Using IN 

-- select *from employees
-- where city in('Pune','Mumbai');

-- Find employees whose department HR or IT Using IN 

-- select *from employees
--  where department in('HR','IT');

-- Where LIKE

-- Find employees whose city start With p

-- select *from employees
-- where city like 'P%';
-- Find employees whose name end  With a

-- select *from employees
-- where name like '%a';

-- Find employees whose city ='Pu_e';
-- select *from employees
-- where city like 'Pu_e';
