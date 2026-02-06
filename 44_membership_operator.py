# membership operator => used to test whether a value or variable is found in sequence 
#                        (string,list,tuple,set,or dictionary)
#                        1) in 
#                        2) not in 


# 1) in 
word = "APPLE" # string
letter = input("guess a letter in the secret word: ")

if letter in word:
    print(f"there is a {letter}")
else:
    print(f"{letter} was not found")


 # 2) not in
word1 = "APPLE"
letter1 = input("guess a letter in the secret word: ")

if letter1  not in word1:
    print(f"{letter1} was not found")
else:
    print(f"there is a {letter1}")
    
# dictionary

capitals = {"INDIA" : "NWE DELHI",
            "USA" : "WASHINGTON BC",
            "CHINA" : "BEIJING",
            "RUSSIA" : "MOSCOW"}
country = input("enter the name of country : ").upper()

if country in capitals:
    print(f"the capital of {country} is {capitals[country]}")
else:
    print(f"{country} not found in the dictionary")
    

email = "teju@gmail.com"

if "@" in email and "." in email:
    print("valid email")
else:
    print("invalid email")