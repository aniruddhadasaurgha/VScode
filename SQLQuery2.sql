
CREATE DATABASE Student_Grouping_Project;
USE Student_Grouping_Project;


CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(50),
    Class VARCHAR(10),
    Subject VARCHAR(20),
    Marks INT,
    Gender VARCHAR(10)
);

INSERT INTO Students VALUES
(1, 'Arjun', '10A', 'Math', 85, 'Male'),
(2, 'Riya', '10A', 'Math', 92, 'Female'),
(3, 'Kabir', '10A', 'Science', 78, 'Male'),
(4, 'Ananya', '10B', 'Math', 88, 'Female'),
(5, 'Rahul', '10B', 'Science', 67, 'Male'),
(6, 'Sneha', '10B', 'Science', 91, 'Female'),
(7, 'Aman', '10C', 'Math', 73, 'Male'),
(8, 'Pooja', '10C', 'Science', 84, 'Female'),
(9, 'Rohit', '10C', 'Math', 95, 'Male'),
(10, 'Neha', '10A', 'Science', 89, 'Female');

SELECT Class, COUNT(*) AS Total_Students
FROM Students
GROUP BY Class;


SELECT Subject, AVG(Marks) AS Average_Marks
FROM Students
GROUP BY Subject;


SELECT Class, MAX(Marks) AS Highest_Marks
FROM Students
GROUP BY Class;


SELECT Class, AVG(Marks) AS Avg_Marks
FROM Students
GROUP BY Class
HAVING AVG(Marks) > 80;

SELECT Gender, COUNT(*) AS Total_Students
FROM Students
GROUP BY Gender;


SELECT Subject, SUM(Marks) AS Total_Marks
FROM Students
WHERE Subject = 'Science'
GROUP BY Subject;


SELECT Class, COUNT(*) AS Student_Count
FROM Students
GROUP BY Class
HAVING COUNT(*) > 3;


SELECT Subject, AVG(Marks) AS Avg_Marks
FROM Students
WHERE Gender = 'Female'
GROUP BY Subject;
