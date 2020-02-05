try :
    f=open("does.txt")
except Exception as e:
    print(e)
else:
    print("Only run if exception not occure or except block did not run")
finally:
    print("Always ocuure")
