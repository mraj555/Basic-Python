class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def methods(self):
        print("Hi.My Name is " + self.name)


h1 = Human("Sherlock", 6)
print(h1.name)
print(h1.age)

h1.methods()
