CREATE DATABASE DXC;

CREATE TABLE DXC_Employees (
	Employee_name varchar(75),
	Employee_ID int, 
	Designation varchar(50),
	Salary float,
	);

INSERT INTO DXC_Employees (Employee_name, Employee_ID, Designation, Salary) VALUES

('Barun', 200518, 'CEO', 100000.00),
('Arun', 250685, 'Manager', 50000.00),
('Natun', 248103 , 'Assistant Manager', 40000.00),
('Tarun', 216767, 'Accountant', 25000.00),
('Karun', 235974, 'Clerk', 20000.00);

SELECT * FROM DXC_Employees;







