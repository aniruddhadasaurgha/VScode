tuple = ("Hello World!", 42, 3.14,  [1, 4, 9, 16, 25])
print(tuple)

student_marks = ("Alan", 9, "Roll No.", 104, "Marks", [100, 98, 95, 97, 99])
print(student_marks)
print(student_marks[0]) 
print(student_marks[5])
print(student_marks[5][4])   
print("Marks of", student_marks[0], "are", student_marks[5]) 
print("Sliced tuple:", student_marks[1:4])
print("Sliced tuple:", student_marks[3:])
print("Sliced tuple:", student_marks[:4])

print("Adding the bonus mark 1, new mark of student is:")

for i in student_marks[5]:
    print(i+1, end=" ")
