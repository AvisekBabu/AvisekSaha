# Tutorial
# Class = Templates
# Object = Instance of a class

# DRY Concept = Do not repeat yourself

## Templates
class Student:
    no_of_leaves = 10

    def __init__(self, aname, adepartment, asalary):
        self.name = aname
        self.department = adepartment
        self.salary = asalary


#    def employee_details(self):
#        return f"Name is {self.name}, department is {self.department}, salary is {self.salary}"

#    def employee_work(self):
#        return f"Work as {self.department}"

## object/instance
harry = Student("Harry", "HR", 35000)
# larry = Student()

## instance variable

# harry.name = "Harry"
# harry.department = "Account"
# harry.salary = 45000

# larry.name = "Larry"
# larry.department = "HR"
# larry.salary = 30000

#print(harry.__dict__)
# print(larry.employee_details())
print(harry.no_of_leaves)
harry.no_of_leaves = 12
print(harry.salary)
