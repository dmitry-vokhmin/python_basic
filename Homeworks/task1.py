"""
1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков)
для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц)
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""

import random

class Matrix:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2
        self.string = ""
        self.matrix = []

    def get_matrix(self):
        self.matrix = [[random.randint(0, 10) for i in range(self.list2)] for x in range(self.list1)]
        for i in self.matrix:
                matrix1 = " ".join(str(itm) for itm in i)
                self.string = self.string + matrix1 + "\n"

    def __add__(self, other):
        count = 0
        new_matrix = []
        while count != len(self.matrix):
            a = [x + y for x, y in zip(self.matrix[count], other.matrix[count])]
            new_matrix.append(a)
            count += 1
        return new_matrix

    def __str__(self):
        return self.string

a = Matrix(4, 3)
a.get_matrix()
b = Matrix(4, 3)
b.get_matrix()
c = a + b
print(a)
print(b)
print(c)