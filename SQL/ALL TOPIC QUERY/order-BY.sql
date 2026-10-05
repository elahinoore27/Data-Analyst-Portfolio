use ecom;
CREATE TABLE employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(150) UNIQUE,
    name VARCHAR(100) NOT NULL,
    age INT CHECK (age >= 18),
    department VARCHAR(50) DEFAULT 'General',
    salary DECIMAL(10,2) CHECK (salary > 0),
    joining_date DATE DEFAULT (CURRENT_DATE)
);
insert into employees(email,name,age,salary) values('noore@gmail.com','amit',25,34445);
select *from employees;
