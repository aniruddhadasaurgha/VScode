student_dictionary = {"name" : "Alex", "age" : 15, "grade" : 9, "roll_number" : 4, "id" : 12345}
print(student_dictionary)
print("Grade is : ",student_dictionary["grade"])
student_dictionary["age"] = 16
student_dictionary["grade"] = 10
print(student_dictionary)
student_dictionary["school"] = "ABC High School and College" 
print(student_dictionary)
student_dictionary.pop("id")
print(student_dictionary)
student_dictionary.clear()
print(student_dictionary)