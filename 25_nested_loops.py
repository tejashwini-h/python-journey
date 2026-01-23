# a loop within another loop (outer,inner)
#  outer loop:
#       inner loop:

rows = int(input("enetr the # of rows: "))
columns= int(input("enetr the # of columns: "))
symbol=input("enter a symnol to use: ")
for x in range(rows):
    for y in range(columns):
        print(symbol,end="")
        
    print()