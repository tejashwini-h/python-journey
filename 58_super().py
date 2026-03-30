# super() = function used in a child to call methods from a parent class (superclass)
#           allows you to extend the functionality of the inherited methods

class shape:
    def __init__(self,color,filled):
        self.color = color
        self.filled = filled
        
    def describe(self):
        print(f"its {self.color} and {'filled' if self.filled else 'not filled'}.")

class circle(shape):
    def __init__(self,color,filled,radius):
        super().__init__(color,filled)
        self.radius = radius
    def describe(self):
        print(f"area = {3.14 * self.radius**2}")
        # if we dont call parent class thn parent method wll not be executed only the the child method will be executed
        
class square(shape):
    def __init__(self,color,filled,width):
        super().__init__(color,filled)
        self.width = width
    def describe(self):
        print(f"area = {self.width**2}")
        super().describe()# this will call the describe method of the parent class

class triangle(shape):
    def __init__(self,color,filled,length,breadth):
        super().__init__(color,filled)
        self.filled = filled
        self.length = length
        self.breadth = breadth
    def describe(self):
        print(f"area = {self.length * self.breadth /2}")
        super().describe()# this will call the describe method of the parent class


circle1 = circle("red",True, 5)
print(circle1.color)
print(circle1.filled)
print(circle1.radius)

square1 = square("blue",False,4)
print(square1.color)
print(square1.filled)
print(square1.width)

triangle1 = triangle("green",True,3,4)
print(triangle1.color)
print(triangle1.filled)
print(triangle1.length)
print(triangle1.breadth)

circle1.describe() 
square1.describe()
triangle1.describe()
# here the child class wll be called not the parent class but 
#we can call the parent class method using super() function 