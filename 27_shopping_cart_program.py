foods =[] # we are not using tuple or set , since tuple are unchangeable , and set are unordered
prices = []
total = 0

while True:
    food = input("enter a food to buy(q to quit): ")
    if food.lower() == "q": # here we are using .lower ,  to even accept the capital "Q"
        break
    else:
        price = float(input(f"enter the price of a {food}: Rs."))
        foods.append(food)
        prices.append(price)
        
print("----- YOUR CART -----")

for food in foods:
    print(food , end = " ") # end to display all the elements in one line
    
for price in prices:
    total += price 
    
print()
print(f"Your total is: Rs.{total}")