# module = > a file containing code you want to include in your program , 
#           use "import" to include a module(built-in or your own)
#           useful to break up a large program reusable separate files
# this main is the file , where i'm creating a my own import function 

import math
import math as m 
print(m.pi)
print()

from math import pi
print(pi)
print()

from math import e
print(e)
a,b,c,d,e = 1,2,3,4,5
print(e ** a)
print(e ** b)
print(e ** c)
print(e ** d)
print(e ** e)
