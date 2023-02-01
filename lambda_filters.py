# Lambda Function
x = lambda a, b: a + b + 20
print(x(85, 20))


def f1(n):
    return lambda a: a * n


doub = f1(3)
print(doub(11))


# Filter Function
def prime(x):
    for n in range(2, x):
        if x % n == 0:
            return False
        else:
            return True


filtered = filter(prime, range(10))
print("Prime numbers are: ", list(filtered))


# Map Function
def square(x):
    return x * x


numbers = [1, 2, 3, 4, 5]
list_squares = map(square, numbers)
print(list(list_squares))
