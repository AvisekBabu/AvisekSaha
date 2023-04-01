#Templates
class Employee:
    no_of_leaves = 9

    def __init__(self, ename, edep):
        self.dep = edep
        self.name = ename

    @classmethod
    def change_of_leaves(cls,eno_of_leaves):
        cls.no_of_leaves = eno_of_leaves

#    def employee_identity(self):
#        return f"{self.name}"
#    def employee_department(self):
#        return f"{self.dep}"

#Object/instance
harry = Employee("Harry Johnson", "HR")
larry = Employee("Larry Anderson", "Accountant")
marry = Employee("Marry Stephen", "Manager")

#print(harry.dep)
#instance variable
#harry.name = "Harry Johnson"
#harry.dep = "HR"

#larry.name = "Larry Anderson"
#larry.dep = "Accountant"

#marry.name = "Marry Stephen"
#marry.dep = "Manager"

#harry.no_of_leaves = 10
#print(harry.__dict__)
#print(harry.no_of_leaves)
#print(marry.employee_department())

print(larry.employee.name)
#harry.change_of_leaves(15)
#print(larry.no_of_leaves)