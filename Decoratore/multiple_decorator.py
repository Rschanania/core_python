"""def Upper_str(func):
    def inner():
        str1=func()
        return str1.upper()
    return inner
def  split_str(func):
    def inner():
        str2=func()
        return str2.split(" ")
    return inner

@split_str
@Upper_str
def ordinary():
    return "Hey How Are ...."

print(ordinary())"""

def upper_s(func):
    def inner():
        str=func()
        return str.upper()
    return inner

@upper_s
def ordinary():
    return "Good Morning"


print(ordinary())