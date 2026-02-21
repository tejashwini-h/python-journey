# list comprehension = a concise way to create lists in python
#                      compact and easier  to read than traditional loops
#                       [expression for value in iterable if condition]
# provides a concise  and efficient way to create new list by applying an expression 
# to each item in an existing iterables,optionally filtering the item
import math 
doubles =[]
for x in range(1,11):
    doubles.append(x*2)
    
print(doubles,end=" ")

square = []
for x in range(1,20,2):
    square.append(x**2)
    
print(square,end=" ")

# list comprehension = 
#  doubles =[expression for value in iterable if condition]
#                ||      ||   ||  ||    ||    
doubles    =[    x*2    for value in range(1,11)          ] # condition later
print(doubles)

fruits = ["apple","orange","banana","coconut"]
fruits=[fruits.upper() for fruit in fruits]
print(fruits)

fruits1=[fruits1.upper() for fruit in ["apple","orange","banana","coconut"]]
print(fruits1)

numbers = [1,-2,3,-4,5,-6]
positive_num=[ num for num in numbers if num >=0]
negative_num=[ num for num in numbers if num <=0]
even_num=[ num for num in numbers if num %2==0]
odd_num=[ num for num in numbers if num %2 !=0]
print(positive_num)
print(negative_num)
print(even_num)
print(odd_num)