#Templates
class Employee:
    no_of_CL = 10
    no_of_EL = 12

    def __init__(self, ename, edesignation, esalary, eWFH, eWFO):
        self.name = ename
        self.designation = edesignation
        self.salary = esalary
        self.WFH = eWFH
        self.WFO = eWFO
    @classmethod
    def change_of_leaves(cls, casual_leave):
        cls.no_of_CL = casual_leave


    def Employee_details(self):
        return f"Name is {self.name}, position is {self.designation}"
    def Employee_working_days(self):
        return f"Work from home {self.WFH}, Work from office {self.WFO}"


#objects/instances
harry = Employee("Harry Johnshon", "HR", 30000, 10, 9)
larry = Employee("Larry Johnshon", "Accountant", 20000, 11, 8)
marry = Employee("Larry Johnshon", "Accountant", 20000, 11, 8)

#instance variables
#harry.name = "Harry Johnshon"
#harry.designation = "HR"
#harry.salary = 30000
#harry.WFH = 10
#harry.WFO = 9

#larry.name = "Larry Johnshon"
#larry.designation = "Accountant"
#larry.salary = 20000
#larry.WFH = 11
#larry.WFO = 8


#marry.name = "Marry Johnshon"
#marry.designation = "HR"
#marry.salary = 25000

#print(Employee.no_of_CL)
#print(marry.__dict__)

#Templates variables
#Employee.no_of_CL = 15
#print(Employee.no_of_CL)
#print(marry.Employee_working_days())

#harry.change_of_leaves(34)
#print(marry.no_of_CL)
#print(harry.salary())