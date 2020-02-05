def outer(expr):
    def inner(func):
        def f():
            return func()+expr
        return f
    return inner

@outer("Ravinder Singh")
def ordinary():
    return "Good Morning "
print(ordinary())