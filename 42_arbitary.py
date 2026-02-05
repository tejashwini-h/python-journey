# arbitrary = varying amount of arguments
#parameters => args , kwargs
# *args =>(argument) allows you to pass multiple non-key arguments
#       => also called as positional arguments
# *kwargs =>(key word arguments)  allows you to pass multiple keyword-arguments
#            * unpacking operator
#         => also called as keyword arguments

# on replacing parameter with args , whn we usw unpacking operator , will pack all the values into tuple


def add(*args): #<class 'tuple'>
    
    print(type(args))
    total = 0
    for arg in args:
        total += arg
    return total


print(add(1,2,3,4,5))

print(add(1,2,3))

print(add(1))
print("--------------------------------------")
def display_name( *names):
    for name in names:
        print(name, end=" ")
        
       
display_name("tejashwini","h" ," naduvinamath")
print()
display_name("tejashwini" ," naduvinamath")
print()
display_name("tejashwini" )
display_name("tejashwini","h","n" ," naduvinamath")
print()
display_name("tejashwini","tej" ," naduvinamath")
print()
print("--------------------------------------")
def print_address(**kwargs):
    print(type(kwargs))
    for values in kwargs.values():
        print(values)
    print("--------------------------------------")
    for keys in kwargs.keys():
        print(keys)
        
    print("--------------------------------------")
    for keys,values in kwargs.items():
        print(f"{keys} : {values}")
    print("--------------------------------------")    
print_address(street = "123 ward",
              city   = "bengaluru" ,
              state  = "karnataka",
              zip    = "560085")

# args and kwargs together
def name_print_address(*args,**kwargs):
    for arg in args:
        print(arg,end = " ")
    print()
    for keys,values in kwargs.items():
        print(f"{keys} : {values}")
    print()
    for values in kwargs.values():
        print(values,end =" ")
    print()
    for keys in kwargs.keys():
        print(keys, end =" ")
    print()
    
    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city',)} {kwargs.get('state',)} {kwargs.get('zip',)}")
    
        
name_print_address("tejashwini","h" ," naduvinamath",
              street = "123 ward",
              city   = "bengaluru" ,
              state  = "karnataka",
              zip    = "560085")
     