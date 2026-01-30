import random

number = random.randint(1,20) # gives only random integer number
number = random.random() # gives floating numbers and it wont take any number , has a default value (0 to 1) 

low = 1
high = 100
number = random.randint(low, high)

options = ("rock","paper","scissors")
option = random.choice(options)

cards = ["2","3",4,5,6,7,"k","q","j"]
random.shuffle(cards)
print(cards)
