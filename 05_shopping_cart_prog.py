item =input("what item would u like to buy? ")
price =float(input("what is the price?: "))
quantity=int(input("how many would u like?: "))
total = price*quantity
print(f"you have bought {quantity} { item}")
print(f"your total is = ${total}")