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

    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))    ### This is one liner
#        params = string.split("-")       ## Params convert into list, wil do split on "-" (dash)
#        print(params)                    ## Can see the result for reference
#        return cls(params[0], params[1], params[2], params[3], params[4])


    def Employee_details(self):
        return f"Name is {self.name}, position is {self.designation}"
    def Employee_working_days(self):
        return f"Work from home {self.WFH}, Work from office {self.WFO}"


#objects/instances
harry = Employee("Harry Johnshon", "HR", 30000, 10, 9)
larry = Employee("Larry Johnshon", "Accountant", 20000, 11, 8)
marry = Employee.from_dash("Marry Johnshon-Accountant-30000-12-10")

print(marry.name)
print(marry.salary)