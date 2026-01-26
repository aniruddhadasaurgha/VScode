CREATE DATABASE School_Aggregate_Project;

USE School_Aggregate_Project;

CREATE TABLE Students (
    Roll_No INT,
    Student_Name VARCHAR(50),
    Marks INT,
    Class VARCHAR(10)
);

INSERT INTO Students (Roll_No, Student_Name, Marks, Class) VALUES
(1, 'Arnab', 100, '10'),
(2, 'Sauda', 96, '10'),
(3, 'Turjo', 97, '10'),
(4, 'Aurgha', 97, '10'),
(5, 'Farhan', 97, '10'),
(6, 'Shuvo', 88, '10'),
(7, 'Adrita', 90, '10'),
(8, 'Saba', 81, '10'),
(9, 'Disha', 95, '10'),
(10, 'Albab', 69, '10');

-- COUNT
SELECT COUNT(*) AS Total_Students
FROM Students;

-- SUM
SELECT SUM(Marks) AS Total_Marks
FROM Students;

-- AVG
SELECT AVG(Marks) AS Average_Marks
FROM Students;

-- MAX
SELECT MAX(Marks) AS Highest_Marks
FROM Students;

-- MIN
SELECT MIN(Marks) AS Lowest_Marks
FROM Students;

-- Aggregate functions with WHERE
SELECT AVG(Marks) AS Avg_Marks_Above_80
FROM Students
WHERE Marks > 80;

-- Aggregate functions with GROUP BY
SELECT Class, COUNT(*) AS Total_Students
FROM Students
GROUP BY Class;

SELECT Class, AVG(Marks) AS Average_Marks
FROM Students
GROUP BY Class;

SELECT Class, MAX(Marks) AS Highest_Marks
FROM Students
GROUP BY Class;

-- GROUP BY with HAVING
SELECT Class, AVG(Marks) AS Average_Marks
FROM Students
GROUP BY Class
HAVING AVG(Marks) > 80;

-- Multiple aggregate functions together
SELECT 
    COUNT(*) AS Total_Students,
    SUM(Marks) AS Total_Marks,
    AVG(Marks) AS Average_Marks,
    MAX(Marks) AS Highest_Marks,
    MIN(Marks) AS Lowest_Marks
FROM Students;
