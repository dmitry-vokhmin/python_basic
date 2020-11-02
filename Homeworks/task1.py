while True:
    a = input("Введите первое число")
    b = input("Введите второе число")
    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        break
    print("Ошибка введено не число")

def div(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
            print("На ноль делить нельзя")

c = div(a, b)
print(c)