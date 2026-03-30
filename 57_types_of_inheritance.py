# multiple inheritance : inherit from more then one class
#                         C(A,B)
# multilevel inheritance : inherit from parent which inherit from another parent
#                           C(B) <- B(A) <- A , 'A' i grandparent
# in python we can have more then one parent


class animal():# grandparent
    def eat(self):
        print("this animal is eating")
        
    def sleep(self):
        print("this animal is sleeping")
        
class prey(animal):#parent
    def flee(self):
        print("this animal is fleeing")

class predator(animal):#parent
    def hunt(self):
        print("thi animal is hunting")

class rabbit(prey):#child
    pass

class hawk(predator):#child
    pass

class fish(predator,prey):#child
    pass

r = rabbit()
h = hawk()
f = fish()

f.hunt()
f.flee()
r.flee()
h.hunt()
r.eat()
r.sleep()
