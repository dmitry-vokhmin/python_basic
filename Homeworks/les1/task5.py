income = int(input("Введите выручку компании"))
losses = int(input("Введите издержки компании"))
profit = income - losses
profitabil = (profit / income) * 100


if income > losses:
    print("Выручка больше издержек")
    print("Рентабельность выручки = " + str(profitabil) + "%")
else:
    print("Издержки больше выручки")

employee = int(input("Введите количество сотрудников в фирме"))
emp_profit = profit / employee
print("Прибыль фирмы в расчете на одного сотрудника " + str(emp_profit))