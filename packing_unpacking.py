def fun(a,b,c,d):
    print(a,b,c,d)

d={"b":4,"d":5,"c":6}
fun(5,**d)
#for the packing the

def Pac(**kwargs):
    print(type(kwargs))
    for key in kwargs:
        print("%s = %s "%(key,kwargs[key]))


Pac(name="Ravinder Singh",ID="14BCS1369",language="Python")
