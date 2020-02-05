# def print_name(Prefix):
#     print("Searching prefix:{}".format(Prefix))
#     while True:
#         name=(yield )
#         if Prefix in name:
#             print(name)
#
#
# corou = print_name("Dear")
#
# corou.__next__()
#
#
# corou.send("Atul")
# corou.send("Dear Atul")


def Search_Name():
    import time
    Name="Ravinder ,Vijender,Narendra,Rana,Rishab"
    print("Delay for few seconds")
    time.sleep(4)
    while True:
        text=yield
        if text in Name:
            print("Yes,This Student is present")
        else:
            print("You send Wrong data")


cr=Search_Name()
next(cr)
cr.send("Ravinder")
cr.send("Rajo")