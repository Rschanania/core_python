class Test:
    def __init__(self,limit):
        self.limit=limit

    def __iter__(self):
        self.x=10
        return self
    def __next__(self):
        x=self.x
        if x>self.limit:
            raise StopIteration("You loop corsed the limit ")
        else:
            self.x=x+1
            return  x



for i in Test(5):
    print(i)
