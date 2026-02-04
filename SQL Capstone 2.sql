CREATE DATABASE BMARPC;
USE BMARPC;
CREATE TABLE Students_of_Class_10 (
	Roll_No INT,
    Student_Name VARCHAR(50),
    Marks INT,
    Class VARCHAR(10)

);

INSERT INTO Students_of_Class_10 (Roll_No, Student_Name, Marks, Class) VALUES
(1, 'Arnab', 85, '10'),
(2, 'Sauda', 78, '10'),
(3, 'Turjo', 92, '10'),
(4, 'Aurgha', 88, '10'),
(5, 'Farhan', 67, '10'),
(6, 'Shuvo', 74, '10'),
(7, 'Adrita', 90, '10'),
(8, 'Saba', 81, '10'),
(9, 'Disha', 95, '10'),
(10, 'Albab', 69, '10');

SELECT * FROM Students_of_Class_10;

SELECT DISTINCT Class FROM Students_of_Class_10;

SELECT Student_Name FROM Students_of_Class_10
WHERE Student_Name LIKE 'A%';

SELECT Student_Name FROM Students_of_Class_10
WHERE Student_Name LIKE '%a';

SELECT Student_Name FROM Students_of_Class_10
WHERE Student_Name LIKE '%ab%';

SELECT Student_Name, Marks
FROM Students_of_Class_10
WHERE Marks > 80
ORDER BY Marks DESC;

SELECT Student_Name, Marks
FROM Students_of_Class_10
WHERE Marks BETWEEN 70 AND 90
ORDER BY Student_Name ASC;

SELECT Student_Name, Marks
FROM Students_of_Class_10
ORDER BY Marks ASC;

SELECT Student_Name, Marks
FROM Students_of_Class_10
ORDER BY Marks DESC;

SELECT DISTINCT Marks
FROM Students_of_Class_10
ORDER BY Marks DESC;

SELECT Student_Name, Marks
FROM Students_of_Class_10
WHERE Student_Name LIKE '_u%';

SELECT Student_Name, Marks
FROM Students_of_Class_10
WHERE Marks >= 85
ORDER BY Marks DESC;

SELECT Student_Name
FROM Students_of_Class_10
WHERE Marks = (
    SELECT MAX(Marks) FROM Students_of_Class_10
);

SELECT Student_Name
FROM Students_of_Class_10
WHERE Marks = (
    SELECT MIN(Marks) FROM Students_of_Class_10
);

SELECT COUNT(*) FROM Students_of_Class_10;

SELECT AVG(Marks) FROM Students_of_Class_10;

SELECT Student_Name, Marks
FROM Students_of_Class_10
WHERE Student_Name LIKE '%a%'
ORDER BY Student_Name;
