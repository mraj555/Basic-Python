# Ordered, Changeable and Allow Duplicates
customList = ["Car", "Bike", 30, 40, 3.0, True, "Bike"]
print(customList)

print(len(customList))

# For Replace Specific Index Item
customList[3] = "Scooters"

# For Insert Specific Index Item
customList.insert(3, "Shine")

# For Insert Item at Last
customList.append("Oranges")

print(customList[3])
print(customList[1:4])
print(customList[:7])
print(customList[3:])

print(type(customList))
