#indexing = accessing elements of a sequence using [](indexing operator)
#          by using 3 fills [start:end:step] 
#          we can access starting or ending at step

credit_num="1234-567-8910"
print(credit_num[0]) #o/p: 1
print(credit_num[3]) #o/p: 4
print(credit_num[5]) #o/p: 5
print(credit_num[8]) #o/p: -
print(credit_num[0:5]) #o/p: 1234-
print(credit_num[7:11]) #o/p: 7-89
print(credit_num[:5]) #o/p: 1234-
print(credit_num[5:]) #o/p: 567-8910
print(credit_num[-1]) #o/p: 0 (printing from last to first)
print(credit_num[::2]) #o/p: 13-6-90
print(credit_num[3:9:2]) #o/p: 457
print(credit_num[3:9:4]) #o/p: 47
#--------------------------------------
last_digits=credit_num[-4:]
print(f"xxxx-xxx-{last_digits}")
#------reverse number-----------------
credit_num=credit_num[::-1]
print(credit_num)