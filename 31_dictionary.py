# dictionary = a collection of {key : value} pairs
#               ordered and changeable , no duplicates

# here keys = country and values = capitals

capitals = {"INDIA" : "NWE DELHI",
            "USA" : "WASHINGTON BC",
            "CHINA" : "BEIJING",
            "RUSSIA" : "MOSCOW"}
print(capitals.get("INDIA"))

capitals.update({"germany" : "berlin"})
capitals.pop("USA")
capitals.popitem() # removes the recently added element
capitals.keys() # prints only keys , display in single line

for key in capitals.keys():# display one after the another , different line
    print(key)
    
capitals.values() # displays only values

capitals.items() # displays in 2d list of tuple
