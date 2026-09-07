```sql
-- ============================================================
-- DELETE, TRUNCATE, DROP - MYSQL PRACTICE
-- ============================================================


-- ============================================================
-- STEP 1: CREATE DATABASE AND TABLE
-- ============================================================

CREATE DATABASE IF NOT EXISTS sql_practice;
USE sql_practice;

DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    salary INT,
    city VARCHAR(50)
);


-- Insert sample data
INSERT INTO employees VALUES
(1, 'Rahul', 'IT', 60000, 'Pune'),
(2, 'Priya', 'HR', 45000, 'Mumbai'),
(3, 'Amit', 'IT', 70000, 'Pune'),
(4, 'Sneha', 'Sales', 50000, 'Delhi'),
(5, 'Vikas', 'HR', 40000, 'Pune');


-- Check the table
SELECT * FROM employees;


-- ============================================================
-- 1. DELETE
-- ============================================================

-- QUESTION:
-- Delete the employee whose emp_id is 5.

-- ANSWER:
DELETE FROM employees
WHERE emp_id = 5;

-- COMMENT:
-- DELETE removes ROWS from the table.
-- The table structure remains.
-- DELETE can use WHERE.
-- Here, only employee 5 is deleted.


-- Check the result
SELECT * FROM employees;


-- ============================================================
-- 2. DELETE ALL ROWS
-- ============================================================

-- First add employee 5 again for practice
INSERT INTO employees VALUES
(5, 'Vikas', 'HR', 40000, 'Pune');


-- QUESTION:
-- Delete ALL employees from the table.

-- ANSWER:
DELETE FROM employees;

-- COMMENT:
-- DELETE without WHERE removes ALL ROWS.
-- The table itself still exists.
-- The columns, structure, and constraints remain.


-- Check the table
SELECT * FROM employees;


-- ============================================================
-- 3. TRUNCATE
-- ============================================================

-- Add data again because DELETE removed it
INSERT INTO employees VALUES
(1, 'Rahul', 'IT', 60000, 'Pune'),
(2, 'Priya', 'HR', 45000, 'Mumbai'),
(3, 'Amit', 'IT', 70000, 'Pune'),
(4, 'Sneha', 'Sales', 50000, 'Delhi'),
(5, 'Vikas', 'HR', 40000, 'Pune');


-- QUESTION:
-- Remove ALL rows using TRUNCATE.

-- ANSWER:
TRUNCATE TABLE employees;

-- COMMENT:
-- TRUNCATE removes ALL ROWS from the table.
-- The table structure remains.
-- You CANNOT use WHERE with TRUNCATE.
-- TRUNCATE is generally faster than DELETE for
-- removing the entire table contents.


-- Check the result
SELECT * FROM employees;


-- ============================================================
-- 4. DROP
-- ============================================================

-- Add data again
INSERT INTO employees VALUES
(1, 'Rahul', 'IT', 60000, 'Pune'),
(2, 'Priya', 'HR', 45000, 'Mumbai'),
(3, 'Amit', 'IT', 70000, 'Pune');


-- QUESTION:
-- Remove the complete employees table.

-- ANSWER:
DROP TABLE employees;

-- COMMENT:
-- DROP removes the ENTIRE TABLE.
-- It removes:
--   1. All rows
--   2. Table structure
--   3. Columns
--   4. Indexes/constraints associated with the table
--
-- After DROP, the employees table no longer exists.


-- This will give an error because the table was dropped:
-- SELECT * FROM employees;


-- ============================================================
-- 5. MAIN DIFFERENCE
-- ============================================================

-- DELETE
-- Removes rows.
-- Table remains.
-- WHERE can be used.

-- Example:
-- DELETE FROM employees WHERE emp_id = 1;


-- TRUNCATE
-- Removes ALL rows.
-- Table remains.
-- WHERE cannot be used.

-- Example:
-- TRUNCATE TABLE employees;


-- DROP
-- Removes the entire table.
-- Table does NOT remain.

-- Example:
-- DROP TABLE employees;


-- ============================================================
-- EASY MEMORY TRICK
-- ============================================================

-- DELETE    = Remove ROWS
-- TRUNCATE  = Empty the TABLE
-- DROP      = Remove the TABLE itself


-- ============================================================
-- FINAL COMPARISON
-- ============================================================

-- DELETE:
-- Data       -> Removed
-- Table      -> Remains
-- WHERE      -> YES

-- TRUNCATE:
-- Data       -> All removed
-- Table      -> Remains
-- WHERE      -> NO

-- DROP:
-- Data       -> Removed
-- Table      -> Removed
-- WHERE      -> NO
```
