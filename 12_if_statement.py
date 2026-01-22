response = input("would you like food? (y/n)")

if response == "y":
    print("have some food :) !!")
else:
    print("noo food for u :( !!") 
name = input("enter your name ")

if name =="":
    print("you did not type in your name !!")
else:
    print(f"hello {name} ")

#boolean
for_sale = True

if for_sale:
    print("this item is for sale")
else:
    print("not for sale")