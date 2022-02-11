# characteristics of object is attribute


# the syntax for creating attribute is
# self.attribute=something

# there is a special method called
# __init__()    #special method

class Dog:
    # class object attribute 
    species='mammals'


    def __init__(self,breed):
        self.breed=breed

a=Dog(breed='pitbull')
print(a.breed)


b=Dog(breed='Shepherd')
print(b.breed)
print(a.species)