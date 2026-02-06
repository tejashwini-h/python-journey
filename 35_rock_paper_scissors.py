import random

options = ("rock","paper","scissors")

running = True

while running:
    player_choice = None
    computer = random.choice(options)  
         
    while player_choice not in options:
        player_choice = input("enter a choice (rock, paper ,scissors): ")


    print(f"player : {player_choice} and computer : {computer}")

    if player_choice==computer:
        print("it's a tie!!!")
    elif player_choice == "rock" and computer=="scissors":
        print("you win!!")
    elif player_choice== "paper" and computer=="rock":
        print("you win!!")
    elif player_choice== "scissors" and computer=="paper":
        print("you win!!")
    else:
        print("you lost!!!")
    
    play_again=input("play again (y/n): ").lower()
    if not play_again =="y":
        running = False
    # if not play_again=input("play again (y/n): ").lower()=="y":
        #running = False
print("thanks for playing!!")