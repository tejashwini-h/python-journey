def show_balance(balance):
    print(f"your balance is Rs.{balance:,.2f}")
    print("****************************")
    print()

def deposit():
    amount = float(input("enter an amount to be deposited : "))
    if amount < 0:
        print("thats not a valid amount")
        print("****************************")
        print()
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("enter an amount to be withdrawn : "))
    if amount > balance:
        print("insufficient funds")
        print("****************************")
        print()
        return 0
    if amount < 0:
        print("thats not a valid amount")
        print("****************************")
        print()
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("****************************")
        print()
        print("banking program")
        print()
        print("1.show balance ")
        print("2.deposit")
        print("3.withdraw")
        print("4.exit")
        print()
        choice =input("enter your choice(1-4): ")
        if choice=='1':
            show_balance(balance)
        elif choice=='2':
            balance = balance + deposit()
        elif choice=='3':
            balance -= withdraw(balance)
        elif choice =='4':
            is_running =False
        else :
            print()
            print("that ia not a valid choice")

    print()    
    print("thank you have a nice day")

if __name__ == '__main__':
    main()