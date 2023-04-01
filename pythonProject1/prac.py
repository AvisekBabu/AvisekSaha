##Templates
class Employee:
    no_of_leaves = 9

    def __int__(self,ename,esalary):
        self.name = ename
        self.salary = esalary


#    def print_details(self):
#        return f"My name is {harry.name}. My salary is {harry.salary}"

harry = Employee("Harry Kumar", 3400)
larry = Employee()


# Instance variable
# harry.name="Harry Kumar"
# harry.salary="2678"

# larry.name="Larry Kumar"
# larry.salary="2300"

print(harry.salary())
