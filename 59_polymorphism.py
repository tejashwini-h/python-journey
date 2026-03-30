# polymorphism = Greek word meaning "many forms"

# can be used to perform the same action in different ways
# can be achieved by inheritance and duck typing
# duck typing = concept where the class of an object is less important than the methods it defines
# object must have the necessary methods and properties to be used for a specific purpose, regardless of its class

from abc import ABC , abstractmethod

class shape:
    @abstractmethod
    def area(self):
        pass

class circle(shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

class square(shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side **2
    
class triangle(shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def area(self):
        return self.base *self.height *0.5
    
class pizza(shape):
    def __init__(self,topping,radius):
        super().__init__(radius) # pizza is considered as shape and the property of circle is inherited
        self.topping = topping
        

shapes = [circle(4) ,square(5),triangle(6,7),pizza("pepperoni" , 15)] # this is an example of polymorphism where we can use the same shape class to create different shapes like circle and square

for shape in shapes:
    print(f"{shape.area()} cm2")