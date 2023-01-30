fruits = ["apples", "bananas", "pineapples", "mango", "Kivy"]
new_fruits = []

for x in fruits:
    if "a" in x:
        new_fruits.append(x.upper())

print(new_fruits)