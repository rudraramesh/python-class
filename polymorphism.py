class Dog:
    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name +' says whoof'


class Cat:
    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name +' says meow'

a=Dog('Teddy')
b=Cat('Oliver')
print(a.speak())
print(b.speak())

