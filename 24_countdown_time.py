import time

my_time=int(input("enter time in seconds: "))

for x in reversed(range(0,my_time)):
    print(x)
    time.sleep(1)# it wont print or do anything for five sec 

print("TIME IS UP !!")


my_time=int(input("enter time in seconds: "))
for x in range(my_time,0,-1):
    print(x)
    time.sleep(1)# it wont print or do anything for five sec 

print("TIME IS UP !!")

my_time=int(input("enter time in seconds: "))
for x in range(my_time,0,-1):
    seconds = x%60
    min=int(x/60)%60
    hrs =int(x/3600)
    print(f"{hrs:02}:{min:02}:{seconds:02}")# 02 : make sures 2 digits , if not adds the zero at the beginning
    time.sleep(1)# it wont print or do anything for five sec 

print("TIME IS UP !!")