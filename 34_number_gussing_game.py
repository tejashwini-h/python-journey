import random
low = 0
high = 100
answer = random.randint(low,high)
guesses =0
is_running = True

print(" number guessing game")
print(f" select a number between {low} and {high}")

while is_running:
    guess =( input("enter ur guess"))
    
    if guess.isdigit():
        guess = int(guess)
        guesses +=1
        
        if guess <low or guess > high:
            print("that no is out of range ")
            print(f" please select a number between {low} and {high}")
        elif guess<answer :
            print(" too low!!! try again")
        elif guess > answer:
            print(" too high !!! try again")
        else:
            print(f"CORRECT! the answer was {answer} ")
            print(f"no. of guesses are {guesses}")
            is_running = False
    else:
        print(" invalid guess")
        print(f" please select a number between {low} and {high}")