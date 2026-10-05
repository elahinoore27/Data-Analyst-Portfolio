create database practice;
use practice;
CREATE TABLE employees (
    emp_id INT,
    emp_name VARCHAR(50),
    department VARCHAR(50),
    salary INT,
    joining_date DATE
);

INSERT INTO employees (emp_id, emp_name, department, salary, joining_date)
VALUES
(1, 'Amit',   'IT',      60000, '2022-01-10'),
(2, 'Rahul',  'IT',      80000, '2021-03-15'),
(3, 'Priya',  'IT',      80000, '2023-06-20'),
(4, 'Neha',   'HR',      50000, '2022-07-01'),
(5, 'Sneha',  'HR',      70000, '2021-05-10'),
(6, 'Raj',    'HR',      70000, '2023-01-12'),
(7, 'Vikas',  'Sales',   45000, '2022-02-18'),
(8, 'Pooja',  'Sales',   55000, '2021-08-25'),
(9, 'Karan',  'Sales',   65000, '2023-04-05'),
(10,'Anita',  'IT',      60000, '2024-02-10');

-- Find the average salary of each department
SELECT
    emp_name,
    department,
    salary,
    AVG(salary) OVER(PARTITION BY department) AS avg_dept_salary
FROM employees;

-- Find the average salary of each department

SELECT
    emp_name,
    department,
    salary,
    MAX(salary) OVER(PARTITION BY department) AS max_dept_salary
FROM employees;

-- Row Number

SELECT
    emp_name,
    department,
    salary,
    ROW_NUMBER() OVER(ORDER BY salary DESC) AS row_num
FROM employees;

-- Rank

SELECT
    emp_name,
    salary,
    RANK() OVER(ORDER BY salary DESC) AS salary_rank
FROM employees;

-- Dense Rsnk

SELECT
    emp_name,
    salary,
    RANK() OVER(ORDER BY salary DESC) AS rank_value,
    DENSE_RANK() OVER(ORDER BY salary DESC) AS dense_rank_value
FROM employees;
-- Find the highest-paid employee in each department

SELECT *
FROM (
    SELECT
        emp_name,
        department,
        salary,
        RANK() OVER(
            PARTITION BY department
            ORDER BY salary DESC
        ) AS rnk
    FROM employees
) x
WHERE rnk = 1;


-- Find the second-highest salary

SELECT *
FROM (
    SELECT
        emp_name,
        salary,
        DENSE_RANK() OVER(ORDER BY salary DESC) AS rnk
    FROM employees
) x
WHERE rnk = 2;

-- Find the top 2 employees from each department
SELECT *
FROM (
    SELECT
        emp_name,
        department,
        salary,
        ROW_NUMBER() OVER(
            PARTITION BY department
            ORDER BY salary DESC
        ) AS rn
    FROM employees
) x
WHERE rn <= 2;

-- Calculate running total of salaries

SELECT
    emp_name,
    salary,
    SUM(salary) OVER(
        ORDER BY emp_id
    ) AS running_salary
FROM employees;

-- Find previous employee's salary using LAG()

SELECT
    emp_name,
    salary,
    LAG(salary) OVER(
        ORDER BY emp_id
    ) AS previous_salary
FROM employees;

-- Find the next employee's salary using LEAD()
SELECT
    emp_name,
    salary,
    LEAD(salary) OVER(
        ORDER BY emp_id
    ) AS next_salary
FROM employees;

-- Find salary difference from previous employee
SELECT
    emp_name,
    salary,
    salary - LAG(salary) OVER(
        ORDER BY emp_id
    ) AS salary_difference
FROM employees;

-- Find employees earning more than their department average

SELECT *
FROM (
    SELECT
        emp_name,
        department,
        salary,
        AVG(salary) OVER(
            PARTITION BY department
        ) AS avg_salary
    FROM employees
) x
WHERE salary > avg_salary;