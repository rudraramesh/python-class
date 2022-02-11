# inheritance is to form new classes from classes that hav been alreaty define . the newly formed classes are called derived class, the class that we derive from are called base class.the derived class override or extend the functionality of base class.


class Animal:
    def __init__(self):
        print('Animal Class Created')

    def whoIs(self):
        print('Animal')
    
    def eat(self):
        print('Animal who eats')


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog class created')


    def whoIs(self):
        print('Dog')


    def bark(self):
        print('woof')


d=Dog()
print(d)
d.whoIs()
d.eat()
    