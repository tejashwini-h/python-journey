# object = a "bundle" of related attributes(variable) and methods(function) 
#           ex. phone,cup,book
#           you need a 'class' to create many object

#class = (blueprint) used to design the structure and layout of an object

class car:
    def __init__(self,model,year,color,for_sale):# this is called constructor method , it is used to construct object
        # self means this object we are creating  it now that is 'car'      
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
    
car1 =car("asta",2024,"white",False) # car1 is a class , we can create a 100"s of class for a 1 single object
print(car1) # o/p <__main__.car object at 0x7d8aba934830> ....memory address of the object will be given
print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)
print("---------------------------")
car2 = car("punto",2012,"gray",True)
print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)
print("---------------------------")
car3 = car1
print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)

def drive1(self):
    print(f"the {self.model} i driving")

def stop(self):
    print(f"you stop  {self.model}  driving")
    
car1 =car("asta",2024,"white",False)
car2 = car("punto",2012,"gray",True)
car3 = car1

car1.drive1()
car1.stop()

car2.drive()
car2.stop()

car3.drive()
car3.stop()
