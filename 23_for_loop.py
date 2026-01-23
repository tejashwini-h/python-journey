# executes a block of code a fixed no. of times
#  we can iterate over a range ,string,sequence,etc.
for x in range(1,7):
    print(x)
    
for counter in range(1,7):
    print(counter)

for x in range(1,7):
    print(x)
print("HAPPY NEW YEAR")

for x in reversed(range(1,7)):
    print(x)
    
for x in range(1,11,2):#in count of 2 , op: 1 3 5 7 9 
    print(x)
    
credit_num="1234-567-8910"
for x in credit_num:
    print(x) # op: number in the form of string wll be placed in row wise 
    
for x in range(1,10):
    if x == 7:
        continue
    else:
        print(x) # here from 1 to 10 only 7 wll be skipped and rest all wll be printed
        
for x in range(1,10):
    if x == 7:
        break
    else:
        print(x) # here from 1 to 10 only till 7 wll be printed , bcz of the break
    
for x in range(1,7):
    print(x,end="") # all the numbers in the one single line 
    print(x,end="-")#op : 1-2-3-4-5-6-7-
    print(x,end=" ")  # op : 1 2 3 4 5 6 7 