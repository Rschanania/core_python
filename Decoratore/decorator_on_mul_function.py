# def dec_div(func):
#     def inner(*args):
#         list1=[]
#         list1=args[1:]
#         if 0 in list1:
#             return "Give an Appropriate Input !!!!"
#         else:
#             return func(*args)
#     return inner
#
#
#
# @dec_div
# def div1(a,b):
#     return a/b
#
# def div2(a,b,c):
#     return a/b/c
#
# print(div1(2,0))

def div(*args):

    res=args[0]
    print(type(args))
    list1=[]
    list1=args[1:]
    if 0 in list1:
        return "Please Enter a Valid Input"
    else:
        for i in range(1,len(args)):
            res=res/args[i]

    return  res

print(div([20,2,2,2,2]))