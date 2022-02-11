#  **kwargs ->it builds a dictionary of key/value pairs
def myFunc(**kwargs):
    if 'fruit' in kwargs:
        print(f"my favourite fruit is {kwargs['fruit']}")

    else:
        print(' i donot like that fruit')

myFunc(fruit='apple')





# try except -> error handling
# scope -> local scope and global scope


# x=25 
# def func():
#     x=20 -> local


# web scraping with python