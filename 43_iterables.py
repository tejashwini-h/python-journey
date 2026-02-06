# iterables = an object/collection that can return its elements one at a time,
#              allowing it to be iterated over in a loop
#              iterables are object , you can loop through

numbers = [1,2,3,4,5]# list are iterables

for number in numbers:
    print(number,end=" ")
print()
    
for number in reversed(numbers):
    print(number,end=" ")
print()

numbers = (1,2,3,4,5)# tuples are also iterables

for number in numbers:
    print(number,end=" ")
print()

for number in reversed(numbers):
    print(number,end=" ")
print()

numbers = {1,2,3,4,5}# sets are also iterables

for number in numbers:
    print(number,end=" ")
print()
    
#for number in reversed(numbers):   reversing of set is not possible
    
name = "Tejashwini H N" # string is also iterable 
for character in name:
    print(character,end = " ")
print()
    
my_dictionary = {"A":1,
                 "B":2,
                 "C":3} 
for key in my_dictionary:
    print(key)
print()
for value in my_dictionary.values():
    print(value)
print()
for key,value in my_dictionary.items():
    print(f"{key} : {value}")
print()