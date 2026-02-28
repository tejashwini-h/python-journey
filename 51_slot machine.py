import random
def spin_row():
    symbols = ['🍒' , ' 🍋' , ' 🍉' , '💡' , ' ⭐']
    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results
# or this 
    #return[random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(" | ".join(row))

def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet *3
        elif row[0] == '🍋':
            return bet*4 
        elif row[0] == '🍉':
            return bet*5 
        elif row[0] == '💡':
            return bet*10
        elif row[0] == '⭐':
            return bet*20
    return 0
            

def main():
    balance =100
    print()
    print("welcome to python slots😀")
    print("symobols: 🍒, 🍋, 🍉, 💡, ⭐")
    print()
    while balance > 0:
        print(f"current balance : Rs.{balance:,}")
        bet =input("place ur bet amount : ")
        
        if not bet.isdigit():
            print("please enter a valid digit")
            continue
        bet =int(bet)
        
        if bet > balance:
            print("insufficient funds")
            continue
        if bet<=0:
            print("bet must be greater thn 0")
            continue
        balance -= bet
        
        row = spin_row()
        print("spinning... \n")
        print_row(row)
        
        payout =get_payout(row,bet)
        
        if payout > 0:
            print(f"you won Rs.{payout}")
        else:
            print("sorry u lost this round")
            
        balance +=payout
        
        play_again = (input("do u want to play again? (y/n)"))
        if play_again != "y":
            break
        
    print(f"game over ! your final balance is Rs.{balance}")
if __name__ == '__main__': 
    main()