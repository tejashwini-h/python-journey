# return = ued to end the function , and send result back to the caller

def add(x,y):
    add =x+y
    return add

def sub(x,y):
    add =x-y
    return add

def multiply(x,y):
    add =x*y
    return add

def divide(x,y):
    add =x/y
    return add

print(add(5,2))
print(sub(5,2))
print(multiply(5,2))
print(divide(5,2))

def create_name(first,last):
    first=first.capitalize()
    last =last.capitalize()
    return first+" "+last

full_name =create_name("tejashwini","naduvinamath")
print(full_name)