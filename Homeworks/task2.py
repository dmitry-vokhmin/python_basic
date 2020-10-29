list = []
i = 0
b = 1

while True:
    value = input("Введите любые данные! Если хотите выйти из функции ввода, напишите 'Stop'")
    if value == "Stop":
        break
    list.append(value)
print(list)

list1 = list[::]

while b < len(list):
    list[i] = list1[b]
    list[b] = list1[i]
    i += 2
    b += 2
print(list)