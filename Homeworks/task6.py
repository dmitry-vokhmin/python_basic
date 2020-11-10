def numbers(content):
    """
    Функция для вычисления суммы цифр из строчки и выделения предмета
    :param content: Принимает строчку текста из файла
    :return: возщает сумму чисел и предмет
    """
    num_list = []
    num = ' '
    sum = 0
    for char in content:
        index = content.index(":")
        subject = content[:index]
        if char.isdigit():
            num = num + char
        else:
            if num != ' ':
                num_list.append(int(num))
                num = ' '
    for itm in num_list:
        sum += itm
    return subject, sum

file = open("task6.1.txt", "r", encoding="utf-8")
content = file.readlines()

my_list = []
for itm in content:
    a, b = numbers(itm)
    my_list.append(a)
    my_list.append(b)

final_dict = {my_list[i]: my_list[i + 1] for i in range(0, len(my_list), 2)}
print(final_dict)

file.close()