CREATE DATABASE Student_SQL_Project;

USE Student_SQL_Project;

CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(50),
    Class VARCHAR(10),
    Age INT,
    Gender VARCHAR(10)
);

CREATE TABLE Scores (
    ScoreID INT PRIMARY KEY,
    StudentID INT,
    Subject VARCHAR(30),
    Marks INT,
    ExamType VARCHAR(20),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
);

INSERT INTO Students VALUES
(1, 'Arjun', '10A', 15, 'Male'),
(2, 'Riya', '10A', 14, 'Female'),
(3, 'Kabir', '10B', 15, 'Male'),
(4, 'Ananya', '10B', 14, 'Female'),
(5, 'Ishaan', '10A', 15, 'Male');

INSERT INTO Scores VALUES
(101, 1, 'Math', 85, 'Midterm'),
(102, 1, 'Science', 78, 'Midterm'),
(103, 2, 'Math', 92, 'Midterm'),
(104, 2, 'Science', 88, 'Midterm'),
(105, 3, 'Math', 67, 'Midterm'),
(106, 3, 'Science', 72, 'Midterm'),
(107, 4, 'Math', 90, 'Midterm'),
(108, 4, 'Science', 95, 'Midterm'),
(109, 5, 'Math', 81, 'Midterm'),
(110, 5, 'Science', 76, 'Midterm');

SELECT * FROM Students;

SELECT * FROM Scores;

SELECT Name, Subject, Marks
FROM Students
JOIN Scores ON Students.StudentID = Scores.StudentID;

SELECT Name, Subject, Marks
FROM Students
JOIN Scores ON Students.StudentID = Scores.StudentID
ORDER BY Marks DESC;

SELECT Name, Subject, Marks
FROM Students
JOIN Scores ON Students.StudentID = Scores.StudentID
WHERE Marks >= 85;

SELECT Class, COUNT(*) AS Total_Students
FROM Students
GROUP BY Class;

SELECT Subject, AVG(Marks) AS Average_Marks
FROM Scores
GROUP BY Subject;

SELECT Subject, MAX(Marks) AS Highest_Marks
FROM Scores
GROUP BY Subject;

SELECT Subject, MIN(Marks) AS Lowest_Marks
FROM Scores
GROUP BY Subject;

SELECT Name, SUM(Marks) AS Total_Marks
FROM Students
JOIN Scores ON Students.StudentID = Scores.StudentID
GROUP BY Name;

SELECT Name, AVG(Marks) AS Average_Marks
FROM Students
JOIN Scores ON Students.StudentID = Scores.StudentID
GROUP BY Name
HAVING AVG(Marks) > 80;

SELECT Gender, AVG(Marks) AS Avg_Marks
FROM Students
JOIN Scores ON Students.StudentID = Scores.StudentID
GROUP BY Gender;

UPDATE Scores
SET Marks = Marks + 5
WHERE Subject = 'Math';

SELECT Name, Subject, Marks
FROM Students
JOIN Scores ON Students.StudentID = Scores.StudentID
WHERE Subject = 'Math';

DELETE FROM Scores
WHERE Marks < 70;

SELECT * FROM Scores;

SELECT Name
FROM Students
WHERE StudentID IN (
    SELECT StudentID
    FROM Scores
    WHERE Marks = (
        SELECT MAX(Marks)
        FROM Scores
    )
);

SELECT Name, Subject, Marks
FROM Students
JOIN Scores ON Students.StudentID = Scores.StudentID
WHERE Marks BETWEEN 80 AND 90;

SELECT DISTINCT Class
FROM Students;

SELECT Name, Subject, Marks
FROM Students
JOIN Scores ON Students.StudentID = Scores.StudentID
ORDER BY Name ASC, Marks DESC;
