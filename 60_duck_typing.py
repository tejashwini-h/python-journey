# duck typing = another way to achieve polymorphism besides inheritance
#               object must have minimum necessary attributes/methods
#               "if it looks like a duck and quacks like a duck, it must be duck"

class animal:
    alive = True
    
class dog(animal):
    def speak(self):
        print("woof !")
        
class cat(animal):
    def speak(self):
        print("meow !")
        
class car:
    alive = False
    def speak(self): # error : AttributeError: 'car' object has no attribute 'speak'
        print("honk !")
    
        
animals = [dog(),cat(),car()]
for animal in animals:
    animal.speak()
    print(animal.alive)
    