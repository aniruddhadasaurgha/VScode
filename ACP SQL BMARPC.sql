CREATE DATABASE BMARPC;

USE BMARPC;

CREATE TABLE Students_of_Class_10_M (
    Roll_No INT,
    Student_Name VARCHAR(50),
    Id_No INT
);

INSERT INTO Students_of_Class_10_M (Roll_No, Student_Name, Id_No) VALUES
(1, 'Arnab', 162998),
(2, 'Sauda', 1604),
(3, 'Turjo', 210998),
(4, 'Aurgha', 200518),
(5, 'Farhan', 19209),
(6, 'Shuvo', 163145),
(7, 'Adrita', 220179),
(8, 'Saba', 171022),
(9, 'Disha', 220328),
(10, 'Albab', 16227);

SELECT * FROM Students_of_Class_10_M;

SELECT * FROM Students_of_Class_10_M
WHERE Student_Name LIKE 'A%';

SELECT * FROM Students_of_Class_10_M
WHERE Student_Name LIKE '%a';

SELECT * FROM Students_of_Class_10_M
WHERE Student_Name LIKE '_u%';

SELECT * FROM Students_of_Class_10_M
WHERE Id_No LIKE '%8';

SELECT * FROM Students_of_Class_10_M
WHERE Id_No LIKE '2___%';

SELECT * FROM Students_of_Class_10_M
WHERE Roll_No BETWEEN 3 AND 7;

SELECT * FROM Students_of_Class_10_M
WHERE Roll_No IN (1, 5, 10);

SELECT * FROM Students_of_Class_10_M
WHERE Roll_No NOT IN (2, 4, 6);

SELECT * FROM Students_of_Class_10_M
WHERE Student_Name LIKE 'S%' AND Roll_No > 5;

SELECT * FROM Students_of_Class_10_M
WHERE Student_Name LIKE '%a%' OR Student_Name LIKE '%o%';

SELECT * FROM Students_of_Class_10_M
WHERE NOT Student_Name LIKE 'A%';

SELECT * FROM Students_of_Class_10_M
ORDER BY Student_Name ASC;

SELECT * FROM Students_of_Class_10_M
ORDER BY Id_No DESC;
