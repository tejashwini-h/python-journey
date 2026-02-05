# collections = single " variable" used to store multiple values
# list = [] ordered and changeable , duplicates ok
#set = {} unordered and immutable , but aa/remove okay , no duplicates
# Tuple = () ordered and unchangeable , duplicate okay , faster


# list => 
fruit = ["apple","orange","banana","coconut"]
print(fruit[0])
print(fruit[1])
print(fruit[2])
print(fruit[3])
print(fruit[0:3])
print(fruit[::2])# this way is called as step , "2" used to display every 2nd element
print(fruit[::-1]) # printing backwards 
for x in fruit:
    print(x)
    
#print(dir(fruit))
print(len(fruit))
print("apple" in fruit)

fruit[0] = "pineapple" # adds at the particular index
for x in fruit:
    print(x)

fruit.append("pineapple") # adds element at the end of the list 
fruit.remove("pineapple")
fruit.insert(2 , " mango")
fruit.sort()
fruit.reverse()
fruit.clear()
fruit.index("mango")


