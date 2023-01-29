# For Loop
numbers = [1, 2, 3, 4, 5, 67, 89, 100]
for x in numbers:
    print(x)
    if x == 5:
        break

a = "Python"
for x in a:
    if x == "t":
        continue
    print(x)

for x in range(50, 100):
    print(x)

# While Loop
i = 1

while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
