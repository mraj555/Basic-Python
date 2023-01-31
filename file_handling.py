
f = open("trial.txt", "r")

# For Reading File
print(f.read())
print(f.readline())

# For Creating and Writing File
y = open("trial.txt", "a")
y.write("A New Line Added")

f.close()
y.close()

# For Removing File
import os

if os.path.exists("trial.txt"):
    os.remove("trial.txt")
else:
    print("File not Exist.");
