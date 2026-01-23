# input() = a function that prompts the user to enter the data returns the entered data as a string
name = input("what is ur name?: ")
age = input("how old are u? :")
# age = int(input("how old are u? :")
age=int(age) # OR directly we can do this 
age = age+1 # if i directly increment without converting thn i'll get error
print(f"hello {name} !!")
print("HAPPY BIRTHDAY :) ")
print(f" age = {age}") 
