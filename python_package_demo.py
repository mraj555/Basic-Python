import camelcase

x= camelcase.CamelCase()

a = "hi there, this is a message to check if the letters of each word are capitalised"

print(x.hump(a))