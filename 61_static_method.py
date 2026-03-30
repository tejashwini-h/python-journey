# static method = a method that belongs to a class rather than any object from that class(instance)
#                 usually used for general utility function
# instants method = best for operation on instants of the class(object)
# static method = best for utility function that do not need access to class data 

class employee:
    
    def __init__(self,name,position):
        self.name = name
        self.position = position
        
    def get_info(self): # this is instant method because it operates on the instance of the class
        return f"{self.name} = {self.position}"
        
    @staticmethod
    def is_valid_position(position): # this is static method because it does not operate on the instance of the class
        valid_positions = ["manager","developer","designer"]
        return position in valid_positions
    
employee1 = employee("john","manager")
employee2 = employee("jane","developer")
employee3 = employee("jack","designer")

print(employee1.get_info()) # john = manager
print(employee2.get_info()) # jane = developer
print(employee3.get_info()) # jack = designer

print(employee.is_valid_position("manager"))  # True
print(employee.is_valid_position("cook"))    # False