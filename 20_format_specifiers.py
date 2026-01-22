# format specifiers = {value:flags} format a value based on what flags are inserted


#.(number)f => round to that many decimal places(fixed points)
# :(number) => allocate that many spaces 
# :03 => allocate and zero pad that many splaces
# :< => left justify
# :> => right justify
# :^ => center align 
# :+ => use a plus sign to indicate values
# := => place sign to leftmost position
# :  => insert a space before a positive numbers
# :, => comma separator

price1 = 3.14235
price2 = -19.123456
price3 = 12.3
print(f"price 1 is {price1:.2f}")
print(f"price 2 is {price2:.2f}")
print(f"price 3 is {price3:.2f}")
#op: price 1 is 3.14
#    price 2 is -19.12
#    price 3 is 12.30
print(f"price 1 is {price1:15}")#op : price 1 is         3.14235
print(f"price 1 is {price1:015}")#op: price 1 is 000000003.14235
print(f"price 1 is {price1:>15}")
print(f"price 2 is {price2:>15}")
print(f"price 3 is {price3:>15}")
# op: price 1 is         3.14235
#     price 2 is      -19.123456
#     price 3 is            12.3
print(f"price 1 is {price1:^15}")
print(f"price 2 is {price2:^15}")
print(f"price 3 is {price3:^15}")
#op : price 1 is |    3.14235    |
#     price 2 is |  -19.123456   |
#     price 3 is |     12.3      |
print(f"price 1 is {price1:+}")
print(f"price 2 is {price2:+}")
print(f"price 3 is {price3:+}")
#op : price 1 is +3.14235
#     price 2 is -19.123456
#     price 3 is +12.3
print(f"price 1 is {price1: }")
print(f"price 2 is {price2: }")
print(f"price 3 is {price3: }")
#op : price 1 is  3.14235
#     price 2 is -19.123456
#     price 3 is  12.3
price1 = 30000.14235
price2 = -19000.123456
price3 = 12000.3
print(f"price 1 is {price1:,}")
print(f"price 2 is {price2:,}")
print(f"price 3 is {price3:,}")
#op : price 1 is 30,000.14235
#     price 2 is -19,000.123456
#     price 3 is 12,000.3
print(f"price 1 is {price1:+,.2f}")
print(f"price 2 is {price2:+,.2f}")
print(f"price 3 is {price3:+,.2f}")
#op : price 1 is +30,000.14
#     price 2 is -19,000.12
#     price 3 is +12,000.30