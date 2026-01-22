#used to evaluate multiple conditions
# or = atleast one condition must be true
# and = both condition must be true
# not inverts the condition (not false,not true)

temp=int(input("enter temp: "))
is_rain = True

if temp>35 or temp<0 or is_rain:
    print(" event cancelled ")
else:
    print("event still scheduled")

temp=int(input("enter temp: "))
is_sunny=input("enter true or false (t,f): ")

if temp>=28 and is_sunny=="t":
    print("hot and sunny")
elif temp<=0 and is_sunny=="t":
    print("cold and sunny")
elif 28>temp>0 and is_sunny=="t":
    print("warm and sunny")
elif temp>=28 and  is_sunny=="f":
    print("hot and not sunny")
elif temp<=0 and is_sunny=="f":
    print("cold and not sunny")
elif 28>temp>0 and  is_sunny=="f":
    print("warm and not sunny")