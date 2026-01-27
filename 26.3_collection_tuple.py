# Tuple = () ordered and unchangeable , duplicate okay , faster#set = {} unordered and immutable , but aa/remove okay , no duplicates

fruit = ("apple","orange","banana","coconut")

print(fruit[0])
print(fruit[1])
print(fruit[2])
print(fruit[3])
print(fruit[0:3])
print(fruit[::2])# this way is called as step , "2" used to display every 2nd element
print(fruit[::-1]) # printing backwards 
for x in fruit:
    print(x)

print(fruit.index("apple") )

#print(dir(fruit))
print(len(fruit))
print("apple" in fruit)

for x in fruit:
    print(x)




