# function -> a block of code to perform a particular task. A function is reusable
#  a function is always define unsing 'def' keyword
#  calling a function with this ()


# define the function
def demo():
    print('hello world')

#  call the function 
demo()


# accepting parameters/arguments

# define te function
def peoplr_name(name):
    print(f'Hello {name}')
    # print('hello '+ name)  #yo ra mathiko yautai ho

# call the function width paramaters
peoplr_name('Ramesh')


# return type

# define 
def add(x,y):
    return x+y


# call the function
abc = add(5,2)
print(abc)