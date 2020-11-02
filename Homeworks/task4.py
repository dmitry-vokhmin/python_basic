def number(x, y):
    n = x ** y
    return n
def number1(x, y):
    count = 1
    n = x
    while count != abs(y):
        x *= n
        count += 1
    return 1 / x

b = number1(3, -5)
a = number(3, -5)
print(a)
print(b)