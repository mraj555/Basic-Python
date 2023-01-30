# Unordered, Changeable and Do Not Allow Duplicates
dict = {"name": "Mr.AJ", "age": 25, "vehicle": "Ford", "DOB": "14-06-1998"}

print(dict)
print(len(dict))
print(type(dict))

# For Getting Value Of Specific Key
x = dict["vehicle"]
print(x)

y = dict.get("name")
print(y)

# For Replacing Value Of Specific Key
dict["vehicle"] = "Bike"
print(dict)

dict.update({"vehicle": "Shine"})
print(dict)

# For Removing Specific Key-Value Pair
dict.pop("vehicle")
print(dict)