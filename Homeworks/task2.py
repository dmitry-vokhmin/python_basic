"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.
"""

class OwnError(Exception):
    def __init__(self, txt=""):
        self.txt = txt

while True:
    inp_data = input("Введите число на которое будем делить 100")
    try:
        inp_data = int(inp_data)
        if inp_data == 0:
            raise OwnError
    except OwnError:
        print("Делить на ноль нельзя")
    except ValueError:
        print("Что то не так")
    else:
        print(f"Результат деления {100 / inp_data}")
        break
