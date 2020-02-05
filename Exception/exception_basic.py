try:
    a=3
    b=int(input("Enter value for b"))
    res=b/(a-3)
    raise ZeroDivisionError("Bhai tune Zero tha Devide Kr diya")
except:
    print("The error is ",)
