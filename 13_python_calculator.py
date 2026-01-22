operator = input("enter an operator(+,-,*,/) ")
num1 = float(input("enter the 1st num "))
num2 = float(input("enter the 2nd num "))

if operator =="+":
    result =num1 + num2
    print(f"result = {result}")
elif operator =="-":
    result =num1 - num2
    print(f"result = {result}")
elif operator =="*":
    result =num1 * num2
    print(f"result = {result}")
elif operator =="/":
    result =num1 / num2
    print(f"result = {result}")
else:
    print(f"{operator} is invalid ")