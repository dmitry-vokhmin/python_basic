month = int(input("Введите номер любого месяца"))
month_list = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

if month in month_list[3:5]:
    print("Spring")
elif month in month_list[6:8]:
    print("Summer")
elif month in month_list[9:11]:
    print("Fall")
elif month in month_list[0:2]:
    print("Winter")

month_dict = {
    12: "Winter",
    1: "Winter",
    2: "Winter",
    3: "Spring",
    4: "Spring",
    5: "Spring",
    6: "Summer",
    7: "Summer",
    8: "Summer",
    9: "Fall",
    10: "Fall",
    11: "Fall",
}

if month in month_dict.keys():
   print(month_dict.get(month))
