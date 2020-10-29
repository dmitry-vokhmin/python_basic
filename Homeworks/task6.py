my_list = []
names = []
price = []
amount = []
measuring = set()
my_tuple = ()

for i in range(int(input("Введите количество товаров"))):
    my_tuple = i + 1, {"Название": input("Название"), "Цена": int(input("Цена")), "Количество": int(input("Кол-во")), "Ед": input("Измерение")}
    my_list.append(my_tuple)



for i in my_list:
    numbers, dict = i
    dict = list(dict.values())
    names.append(dict[0])
    price.append(dict[1])
    amount.append(dict[2])
    measuring.add(dict[3])


result = {
    "Название": names,
    "Цена": price,
    "Количество": amount,
    "Единицы": list(measuring),
}

print(result)







