def fact (n):
    count = 1
    a = 1 # a - это факториал числа
    while count != n:
        a = a * (count + 1)
        count += 1
    for el in range(a):
         yield el

while True:
    number = input("Введите число")
    try:
        number = int(number)
        break
    except ValueError:
        print("Введено не число, повторите ввод")
        continue

count = 0
for el in fact(number):
    if count == number:
        break
    count += 1
    print(el)