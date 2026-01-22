wg = float(input("enter ur weight: "))
unit =input("kilograms or pounds? (k or l): ")

if unit =="k":
    wg=round((wg*2.205),3)
    # we can round it here also wg=round((wg*2.205),3)
    unit="Lbs."
    print(f" your weight is  {wg}{unit} !!!")
elif unit =="l":
    wg=wg/2.205
    unit="Kgs."
    print(f" your weight is  {round(wg,3)}{unit} !!!")
else:
    print(f"{unit} was not valid")
    
