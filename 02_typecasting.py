# typecasting : the process of converting a variable from one data type to another
#                str(), int(), float(), bool()
name = "Tejashwini"
age = 21 
gpa = 8.5
is_student = True

print(type(name)) # tells the data type of variable 
print(type(age))
print(type(gpa))
print(type(is_student))
# o/p = <class 'str'>
#       <class 'int'>
#       <class 'float'>
#       <class 'bool'>

gpa = int(gpa)
print(gpa) # o/p = 8

age = float(age)
print(age)# o/p = 21.0

age =str(age)
print(age)# o/p = 21.0
print(type(age))# o/p = <class 'str'> ( it stores the 21 as "21" in invited comma)

age += "1"
print(age) #o/p: 211

name = bool(name)
print(name) # o/p: true
