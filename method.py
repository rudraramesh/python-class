# methods are function fefined inside the body of the class.they are used to perform the operations with attribute of our objects method are a key concept pf OOP paradigm . for large applications methods are essential.

class Circle:
    pi=3.14
    setRadius=2

    # circle get instantiated with a radius (default 1)
    def __init__(self,radius=1):
        self.radius=radius
        self.area=radius*radius*Circle.pi


    # method for resetting radius
    def setRadius(self,new_radius):
        self.radius=new_radius
        self.area=new_radius*new_radius*self.pi


    # method for getting circumference
    def getCirumference(self):
        return 2*self.pi*self.radius

a=Circle()
a.setRadius(3)
print('Radius is : ',a.radius)
print('area is : ',a.area)
print('cicumference is:',a.getCirumference())

