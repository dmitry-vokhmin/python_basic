condition = True
count = 0
while condition:
    numbers = input(" Введите числа через пробел, для подсчета нажмите ENTER, для выхода 'q'")
    numbers = numbers.split(" ")
    for el in numbers:
        try:
            value = int(el)
            count += value
        except ValueError:
            if el.lower() == "q":
                condition = False
                break
            print("Один или более элементов ввода не является число, повторите ввод")
            break

    print(count)
