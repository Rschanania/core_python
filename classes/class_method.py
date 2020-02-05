class Employee:
    no_of_leave=8#class Variable
    def __init__(self,salary,role):
        self.role=role
        self.salary=salary
    @classmethod
    def change_leave(cls,newLeave,newSalary):
        cls.no_of_leave=newLeave
        cls.salary=newSalary#this is the class variable not the instance variable


ravi=Employee(22222,"Software Developer")
Vijay=Employee("099999","Teacher")

# print(Employee.role) Error bcz it only show the class variable
#if we want to change class Variable without class method it will create an instance veriable it will not change class Variable

ravi.change_leave(11,10)
print(Employee.no_of_leave)
print(Vijay.no_of_leave)


