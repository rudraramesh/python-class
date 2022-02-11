# *args -> when a function parameter starts with an asterik, it allows for an arbitary number of arguements and function takes them in a tuple of values

def myFunc(*args):
    return sum(args)


x=myFunc(20,30,50,60,70)
print(x)
