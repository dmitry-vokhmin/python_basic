"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""

class Date:
    my_dict = {
        "january": 1,
        "february": 2,
        "march": 3,
        "april": 4,
        "may": 5,
        "june": 6,
        "july": 7,
        "august": 8,
        "september": 9,
        "october": 10,
        "november": 11,
        "december": 12,
    }
    def __init__(self, date):
        self.date = date

    @classmethod
    def numbers(cls, date):
        date_list = date.lower().split("-")
        try:
            date_list[1] = cls.my_dict[date_list[1]]
        except:
            date_list[1] = 0
        day, month, year = map(int, date_list)
        cls.validation(day, month, year)
        my_date = f"День:{day} Месяц:{month} Год:{year}"
        return cls(my_date)

    @staticmethod
    def validation(day, month, year):
        if day < 1 or day > 30:
            raise Exception("Не правильный день")
        if month < 1 or month > 12:
            raise Exception("Не правильный месяц")
        if year < 1 or year > 2020:
            raise Exception("Не правильный год")

print(Date.numbers("1-june-2018").date)