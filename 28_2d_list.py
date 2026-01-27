# 2d list : a list made up of a lists
# 2dlist = [ list1 , list2 . list3 , ----]

fruit = ["apple ","orange","banana","coconut"]
vegetables = ["chilli","tomato","onion","carrot"]
meats = ["chicken","fish","mutton","prawn"]
groceries = [fruit,vegetables,meats]

print(groceries)
# op => [['apple ', 'orange', 'banana', 'coconut'], 
#['chilli', 'tomato', 'onion', 'carrot'], 
#['chicken', 'fish', 'mutton', 'prawn']]
print(groceries[0]) # op: ['apple ', 'orange', 'banana', 'coconut']
print(groceries[1]) # op: ['chilli', 'tomato', 'onion', 'carrot']
print(groceries[2]) #op : ['chicken', 'fish', 'mutton', 'prawn']

print(groceries[0][2]) # [r][c] : [0][2] , op => banana

groceries = [['apple ', 'orange', 'banana', 'coconut'], 
             ['chilli', 'tomato', 'onion', 'carrot'], 
             ['chicken', 'fish', 'mutton', 'prawn']]

for collection in groceries:
    print(collection)
    
# op => [['apple ', 'orange', 'banana', 'coconut'], 
#['chilli', 'tomato', 'onion', 'carrot'], 
#['chicken', 'fish', 'mutton', 'prawn']]

for collection in groceries:
    for food in collection:
        print(food , end =" ")
    print()
    
# op => apple  orange banana coconut 
#       chilli tomato onion carrot 
#       chicken fish mutton prawn 