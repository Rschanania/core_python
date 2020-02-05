marks=[31,35,66,77,85]

def Decoratore(fun):
    def disctinct(marks):
        for m in marks:
            if m >= 75:
                print("Disctinction")
            else:
                fun(marks)


    return disctinct


@Decoratore
def result(marks):
    for i in marks:
        if(i<33):
            print("Fail")
            break
    else:
        print("Pass")


Decoratore(result(marks))