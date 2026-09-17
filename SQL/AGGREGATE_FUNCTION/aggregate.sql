use adv;
CREATE TABLE employees (
    emp_id INT,
    name VARCHAR(50),
    department VARCHAR(50),
    salary INT,
    experience INT
);

INSERT INTO employees (emp_id, name, department, salary, experience)
VALUES
(101, 'Amit', 'IT', 60000, 3),
(102, 'Priya', 'HR', 45000, 2),
(103, 'Rahul', 'IT', 75000, 5),
(104, 'Sneha', 'Sales', 50000, 4),
(105, 'Karan', 'HR', 55000, 6),
(106, 'Neha', 'IT', 65000, 4),
(107, 'Rohan', 'Sales', 48000, 2),
(108, 'Pooja', 'Finance', 70000, 5),
(109, 'Arjun', 'Finance', 80000, 7),
(110, 'Meera', 'Sales', 52000, 3);

-- Q1. Find the total number of employees.
select count(*) as total_emp
from employees;

-- Q2. Find the total salary of all employees
select sum(salary) as Total_salary
from employees;

-- Q3. Find the average salary of all employees.

select avg(salary) as average_salary
from employees;


-- Q4. Find the highest salary.

select max(salary) as highest_salary
from employees;

-- Q5. Find the lowest salary

select min(salary) as lowest_salary
from employees;

-- Q6. Find the number of employees in each department.

select department, count(*) as Total_department
from employees
group by department;

-- Q7. Find the total salary paid by each department.
select department, sum(salary) as Total_salary
from employees
group by department;

-- Q8. Find the average salary of each department.
select department, avg(salary) as Total_salary
from employees
group by department;

-- Q9. Find the highest salary in each department

select department, max(salary) as highest
from employees
group by department;

-- Q10. Find the lowest salary in each department.

select department, min(salary) as lowest
from employees
group by department;

-- Q11. Find departments having more than 2 employees.

select department, count(*) as Total_department
from employees
group by department
having count(*)>2;

-- Q12. Find departments where the average salary is
--  greater than 60,000.

select department, avg(salary) as average_salary
from employees
group by department
having avg(salary)>60000;

-- Q13. Find departments where the total salary
-- is greater than 150,000

select department, sum(salary) as average_salary
from employees
group by department
having sum(salary)>150000;

-- Q14. Find the department with the highest average salary.

SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
ORDER BY avg_salary DESC
LIMIT 1;

-- Q15. Find the total salary of employees whose 
-- experience is greater than 3 years
select sum(salary) as total
from employees
where  experience>3;

-- Q16. Average salary of IT employees

select avg(salary) as avg
from employees
where department='IT';

-- Q17. Count employees with salary > 50,000
select count(*) as total_count
from employees
where salary>50000;

-- Q18. Difference between highest and lowest salar

select max(salary)-min(salary) as Diffrence
from employees;