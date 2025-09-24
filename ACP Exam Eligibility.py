work = int(input("Enter total number of work days :"))
absent = int(input("Enter number of days absent :"))
prct = ((work-absent)/work)*100
if prct >= 75:
    print("The student is eligible to sit for the exam")
else:
    print("The student is not eligible to sit for the exam")