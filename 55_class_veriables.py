# class variables = shared among all instance of class
#                   defined outside the constructor
#                   allow you to share date among all objects created from that class

class student:
    class_year = 2024 # this is the class variable
    num_student = 0
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        student.num_student += 1
        
student1 = student("spongebob",30)
student2 = student("patrick",35)

print(student1.name)
print(student1.age)
print(student1.class_year)

print(student2.name)
print(student2.age)
print(student2.class_year)

print(student.class_year)
print(student.num_student)