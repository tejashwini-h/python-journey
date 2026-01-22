#validate user input
# 1. username is not mote then 12 characters
# 2. must not contain spaces
# 3. must not contain digits
user_name = input("enter ur name: ")
if len(user_name)>12:
    print("your name cant be more then 12 characters")
elif not user_name.find(" ")== -1:
    print("ur user name cant contain spaces")
elif not user_name.isalpha():
    print("ur username cant contain digits")
else:
    print(f"Hello {user_name}")