#conditional expression = a one line shortcut for the if-else statement(ternary operator)
#                         print or assign one of 2 values based on the condition
#                         return "x" if condition is true else "y"

num = int(input("enter the 1st num "))
print("positive" if num > 0 else "negative")
result = "even" if num%2==0 else "odd"
print(result)

a = float(input("enter the 1st num "))
b = float(input("enter the 2nd num "))
max_num= a if a>b else b
min_num= a if a<b else b
print(f"max ={max_num}  min={min_num}")

age=float(input("enter age "))
status="adult" if age>=18 else "child"
print(f"status = {status}")