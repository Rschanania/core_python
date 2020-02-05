
#decorator with argument
# class MyDecoratore:
#     def __init__(self,function):
#         self.function=function
#
#     def __call__(self,*args,**kwargs):
#         print("We are inside class")
#         self.function(*args,**kwargs)
#
# @MyDecoratore
# def ordinary(name,messgae):
#     print(f"Hello {name} ---->{messgae}")
#
# ordinary("Ravinder Singh","Good AfterNoon")


class SqureDecoratore:
    def __init__(self,function):
        self.function=function
    def __call__(self, *args, **kwargs):
        print("Sqr of the number is :- ")
        result=self.function(*args, **kwargs)
        return  result
@SqureDecoratore
def sqr(n):
    return n*n
print(sqr(10))

c=SqureDecoratore(sqr(10))
c(sqr(10))