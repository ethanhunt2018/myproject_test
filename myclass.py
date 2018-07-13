#!/usr/bin/python

class Employee:
    # All staffs basic class
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name: ", self.name, ", Salary: ", self.salary)


#Create the first object for class Employee
emp1 = Employee("Ethan", 1000)

#Create the second object for class Employee
emp2 = Employee("Ethan2222", 2000)

emp1.displayEmployee()
emp2.displayEmployee()

print("Total Employee %d" % Employee.empCount)


print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)
