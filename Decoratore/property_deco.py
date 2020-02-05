# class student:
#     def __init__(self,first_name,last_name):
#         self.first_name=first_name
#         self.last_name=last_name
#     @property
#     def email(self):
#         if self.first_name==None or self.last_name==None:
#             return f"Email is not set please give an valis email"
#         else:
#             return (f"The email Address is :-{self.first_name}.{self.last_name}@kaamkr.com")
#     @email.setter
#     def email(self,string):
#         print("Setter is calling")
#         name=string.split("@")[0]
#         self.first_name=name.split(".")[0]
#         self.last_name=name.split(".")[-1]
#     @email.deleter
#     def email(self):
#         self.first_name=None
#         self.last_name=None
#
#
# ravi=student("Ravinder","Singh")
# print(ravi.email)
# ravi.email="Ravi.chanania@Kaamkr.com"
# del ravi.email
# print(ravi.email)
#


class student:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def getValue(self):
        return f"{self.first_name}.{self.last_name}@codeWithharry.com"


    def setValue(self,value):
        name=value.split("@")[0]
        self.first_name=name.split(".")[0]
        self.last_name=name.split(".")[-1]

    def delValue(self):
        print("Deleting email Address")
        self.first_name=None
        self.last_name=None
        print("Email Deleted ")

    email=property(getValue,setValue,delValue)

ravi=student("Ravi","Singh")
print(ravi.email)
ravi.email="Vijy.Pankaj@gmail.com"
print(ravi.email)
del ravi.email