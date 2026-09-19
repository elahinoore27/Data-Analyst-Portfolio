CREATE DATABASE JOINS;
USE JOINS;
CREATE TABLE departments (
    dept_id INT PRIMARY KEY AUTO_INCREMENT,
    dept_name VARCHAR(50) NOT NULL
);
 CREATE TABLE employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_name VARCHAR(50) NOT NULL,
    dept_id INT,
    salary DECIMAL(10,2),
    manager_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);
 INSERT INTO departments (dept_name)
VALUES
('IT'),
('HR'),
('Finance'),
('Marketing'),
('Sales');
 INSERT INTO employees
(emp_name, dept_id, salary, manager_id)
VALUES
('Rahul', 1, 60000, NULL),
('Amit', 1, 70000, 1),
('Priya', 2, 50000, 1),
('Sneha', 2, 55000, 3),
('Vikas', 3, 65000, 1),
('Neha', 4, 45000, 1),
('Arjun', NULL, 40000, 3);



-- 1. Display employee name and department name

select e.emp_name,d.dept_name
from employees as e inner join departments as d
on e.dept_id=d.dept_id; 

-- 2 Display all employees,including those without department

select e.emp_name,d.dept_name
from employees as e left join departments as d
on e.dept_id=d.dept_id;

-- 3 Display all depatments,including those without empoyees

select e.emp_name,d.dept_name
from departments as d left join employees as e
on e.dept_id=d.dept_id;

-- 4 find empolyee who dont have valid department

select e.emp_name,d.dept_name
from employees as e left join departments as d
on e.dept_id=d.dept_id
where d.dept_id is null;

-- 5 find department who dont have no employye

select e.emp_name,d.dept_name
from departments as d left join employees as e
on e.dept_id=d.dept_id
where e.emp_id is null;

-- 6 Find number of employye in each department

select d.dept_name,  count(e.emp_id) as emp_count
from departments as d left join employees as e
on e.dept_id=d.dept_id
group by d.dept_name;

-- 7 Find department having more than 5 employees

select d.dept_name,  count(e.emp_id) as emp_count
from departments as d inner join employees as e
on e.dept_id=d.dept_id
group by d.dept_name
having count(e.emp_id)>1;

-- 8 find average salary of each depatment

select d.dept_name, avg(e.salary) as Average_salary
from departments d inner join employees e
on e.dept_id=d.dept_id
group by d.dept_name;

-- 9 find total salary of each depatment

select d.dept_name, sum(e.salary) as total_salary
from departments d inner join employees e
on e.dept_id=d.dept_id
group by d.dept_name;

-- 10 find department where average salary is greater than 50,000

select d.dept_name, avg(e.salary) as Average_salary
from departments d inner join employees e
on e.dept_id=d.dept_id
group by d.dept_name
having avg(e.salary)>50000;

