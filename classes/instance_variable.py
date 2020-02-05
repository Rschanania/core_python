class Test:
    a=100
    def __init__(self):
        self.x=1
        Test.b=101
    def f1(self):
        Test.c=111
        x=100
    @staticmethod
    def f2(m,n):
        print("Inside static method ",m,n)
    def f3(m,n):
        m.n=n
        print("Inside Instance method ",m.n)


t1=Test()
Test.f2(3,8)