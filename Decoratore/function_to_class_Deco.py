def checK_name(method):
    def inner(name_ref):
        if name_ref.name=="Anil":
            print("Your Child did Not study")
        else:
            method(name_ref)
    return inner


class printClass:
    def __init__(self,name):
        self.name=name
    @checK_name
    def print_name(self):
        print("The User name is :- ",self.name)


p=printClass("Anil")
p.print_name()