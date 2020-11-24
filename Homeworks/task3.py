def save_file(next_file, my_file):
    """
    Записывает сумму в файл
    :param next_file: следующий файл
    :param my_file: сумма подсчитанная из предыдущего файла
    :return:
    """
    with open(next_file, "a") as next_file:
        next_file.write("\n" + my_file)

def sum_number(file_path):
    """
    Функция для вычисления суммы чисел в файле
    :param file_path: путь к первому файлу для вычислений
    :return: возвращает сумму чисел в файле
    """
    with open(file_path, "r") as file:
        my_file = file.read()
        my_file = [int(itm) for itm in my_file.split("\n")]
        my_file = str(sum(my_file))
    return my_file

while int(sum_number("task3.1.txt")) < 10 ** 100:
    first_file = save_file("task3.2.txt", sum_number("task3.1.txt"))
    second_file = save_file("task3.3.txt", sum_number("task3.2.txt"))
    third_file = save_file("task3.1.txt", sum_number("task3.3.txt"))