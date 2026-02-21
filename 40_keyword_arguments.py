# keyword arguments = an arguments preceded by an identifier
#                     helps with readability
#                     order of arguments doesn't matter
#         

def hello(greeting,title,first,last):
    print(f"{greeting}{title}{first}{last}")

#positional arguments    
hello("Hello","Ms.","Tejashwini","Naduvinamth")

# keyword arguments
hello(greeting="Hello",title ="Ms.",first="Tejashwini",last="Naduvinamth")

for x in range(1,11):
    print(x,end = " ") # "end" is keyword here
    
print("1","2","3","4","5", sep= "-") # here separator keyword act as keyword argument
