"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, v, h):
         self.v = v
         self.h = h

    @abstractmethod #@property
    def coat(self):
        return self.v / 6.5 + 0.5

    @abstractmethod  #@property
    def suit(self):
        return 2 * self.h + 0.3

    @abstractmethod #@property
    def cloth_sum(self):
        return self.suit() + self.coat() #return self.suit + self.coat

class Some(Clothes):
    def __init__(self, v, h):
        super().__init__(v, h)

    def coat(self):
        return self.v / 6.5 + 1

    def suit(self):
        return 2 * self.h + 1

    def cloth_sum(self):
        return self.suit() + self.coat()

a = Some(6.5, 1)
print(a.coat()) #print(a.coat)
print(a.suit()) #print(a.suit)
print(a.cloth_sum()) #print(a.cloth_sum)