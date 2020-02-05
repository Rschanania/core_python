class Employee:
    no_of_leave=8#class Variable
    def __init__(self,salary,role):
        self.role=role
        self.salary=salary
    @classmethod
    def change_leave(cls,newLeave,newSalary):
        cls.no_of_leave=newLeave
        cls.salary=newSalary#this is the class variable not the instance variable
    @classmethod
    def Constructor(cls,role,salary):
        return cls(role,salary)
    @classmethod
    def from_desh(cls,string):
        return cls(*string.split("-"))


ravi=Employee(22222,"Software Developer")
Vijay=Employee("099999","Teacher")
ravi=ravi.Constructor("25000","Machine Learning")
#using desh class method
Vijay=Employee.from_desh("8888888-Head Master")
print(ravi.salary)
print(Vijay.role)




