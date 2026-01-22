name = input("enter ur name")# i/p = tej
result = len(name)
print(result) #o/p= 3
result = name.find("T")# occurrence of letter
print(result)#o/p= -1
result = name.rfind("T") #revers occurrence of letter
print(result) #o/p= -1
result = name.capitalize()
print(result)#o/p = Tej
result = name.upper()
print(result)#o/p = TEJ
result = name.lower()
print(result)#o/p = tej
result = name.isdigit()
print(result)#o/p = false , since no digit (returns true or false)
result = name.isalpha()
print(result)#o/p = true , only alphabet no space , no 

cell= input("enter ur cell number")
result= cell.count("-") #i/p: 91- 74115 26234
print(result)
result= cell.replace(" ","*") #i/p: 91- 74115 26234
print(result)

print(help(str))