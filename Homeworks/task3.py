"""
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
"""

class OwnError(Exception):
    def __init__(self, txt="Вы ввели не число"):
        self.txt = txt

my_list = []
while True:
    user_inp = input("Введите число, для выхода введите 'stop'\n>>>")
    try:
        if user_inp.isdigit():
            my_list.append(user_inp)
        elif user_inp == "stop":
            break
        else:
            raise OwnError
    except OwnError:
        print("Вы ввели не число")

print(my_list)