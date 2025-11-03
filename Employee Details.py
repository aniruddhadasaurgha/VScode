class Person(object):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print("My Name:", self.name)
        print("My ID Number is:", self.idnumber)
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        Person.__init__(self, name, idnumber)
        self.salary = salary
        self.post = post

    def display(self):
            Person.display(self)
            print("My Salary is:", self.salary)
            print("My Post is:", self.post)
    
    # Create an employee instance and test it
    emp = Employee("John", "E7876", 50000, "Manager")
    emp.display()