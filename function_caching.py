import time
from functools import lru_cache
@lru_cache(maxsize=3)#maxsize means last three calls will be remember no delay will occure
def some_work(n):
    time.sleep(n)
    return n

if __name__=='__main__':

    print("Now Calling Some_work")
    some_work(3)
    print("Done and calling again ")
    some_work(3)
    print("Called")