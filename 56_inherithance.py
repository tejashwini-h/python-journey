# inheritance = allows a class to inherit attributes and methods from another class
#               helps with the code reusability and extensibility
#               class child(parent)
class animal:
    def __init__(self,name):# constructor method, used to create object, it automatically runs when we create an object 
        self.name = name
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
        
class cat(animal):
    def speak(self):
        print("moew")
class dog(animal):
    def speak(self):
        print("woof")
class mouse(animal):
    def speak(self):
        print("sweek")  

dog = dog("scooby")
cat = cat("garfield")
mouse = mouse("mickey")

print(cat.name)
print(cat.is_alive)
cat.eat()
cat.sleep()

mouse.speak()