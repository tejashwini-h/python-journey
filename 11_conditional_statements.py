# if =  do some code only if some condition is true
#        ELSE do something else

age=int(input("enter ur age "))

if age >=100:
    print("you are too old to signup")
elif age>= 18:
    print("you are now signed up!")
elif age<0:
    print("you haven't born yet !!!")
else:
    print("you must be 18+ to sign up")