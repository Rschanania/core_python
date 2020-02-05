
# class SuperMarket:
#     def fun(self):
#         a=9
#         print(a)
#     def __dir__(self):
#         return  ['customer name',"Customer id "]
#
#
# my_cart=SuperMarket()
# print(dir(my_cart))

#
# def outer(fun):
#     x=4
#     def inner():
#         y=10
#         result=x+y
#         return  result
#     return inner
# def f():
#     return ("Good Morning")
#
# outer(f())


#
# y=10
# def outer():
#     z=4
#     print("Z is ",z)
#     def inner():
#         x=7
#         print("X is :- ",x)
#         print("Y is ",y)
#     inner()
#
# outer()

#Decorator
# def dec_func(func):
#     def dec(x,y):
#         if y==0:
#             return "Zero devision error"
#         else:
#             return func(x,y)
#     return dec
#
#
# @dec_func
# def divsion(a,b):
#     return a/b
#
# print(divsion(10,0))
import functools
def upper_s(func):
    @functools.wraps(func)
    def inner(x):
        res=func(x)+x
        return res
    return inner

@upper_s

def ordinary(x):
    return "Good Morning"
print(ordinary(" MC "))
print(ordinary.__name__)