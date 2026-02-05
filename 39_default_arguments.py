# default arguments = a default values for certain parameter
#                     default is used when that arguments is omitted when we invoke a function
#                     make your functions more flexible , reduces no. of the function
#                     1.positional, 2.DEFAULT, 3.keyword, 4. arbitrary 

import time

def count(start , end):
    for x in range(start ,end+1):
        print(x)
        time.sleep(1)
    print("done!")
    
count(0,10)


def count1(end,start=0):
    for x in range(start ,end+1):
        print(x)
        time.sleep(1)
    print("done!")
    
count1(10)

def count2(end,start=0 ):
    for x in range(start ,end+1):
        print(x)
        time.sleep(1)
    print("done!")
    
count2(25,20)