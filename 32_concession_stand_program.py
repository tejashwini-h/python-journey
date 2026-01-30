# name of dictionary is menu here
menu = {"pizza" : 120,
        "nachos" : 120,
        "popcorn" : 80,
        "fries" : 50,
        "chips" : 30,
        "pretzel" : 150,
        "soda" : 90,
        "lemonade" : 70,}
cart =[]
total = 0
print("----------MENU----------")
print("-------YOUR  CART-------") 
for key , value in menu.items():
    print(f"{key:10} : Rs. {value:.2f}")
print("------------------------")
while True:
    food=input("select an item (q to quit) : ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
     
for food in cart:
    total=total + menu.get(food)
    print(food , end=" ")  
        
print()
print(f"total is : Rs. {total:.2f}")
        