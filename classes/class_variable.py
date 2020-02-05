class Employee:
    no_of_leave=8#class Variable
    def __init__(self,salary,role):
        self.role=role
        self.salary=salary


ravi=Employee(22222,"Software Developer")
Vijay=Employee("099999","Teacher")

# print(Employee.role) Error bcz it only show the class variable

ravi.no_of_leave=10
print(ravi.no_of_leave)
print(Vijay.no_of_leave)
print(Employee.__dict__)
print(ravi.__dict__)


