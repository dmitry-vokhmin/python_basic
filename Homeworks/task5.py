def sum_numbers(number):
    number = number.split(" ")
    num_sum = 0
    try:
        for idx in number:
            num_sum += int(idx)
    except ValueError:
        print("В файле встретились буквы, подсчет остановлен")
    return num_sum

file = open("task5.1.txt", "w")
content = file.write(input("Введите числа через пробел"))
file.close()

file = open("task5.1.txt", "r")
content_1 = file.readline()
result = sum_numbers(content_1)
print(f"Сумма чисел в файле: {result}")
file.close()



