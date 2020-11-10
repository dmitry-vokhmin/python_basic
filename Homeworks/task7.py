import json

def profit(content):
    content = content.split(" ")
    profit = int(content[2]) - int(content[3])
    return profit

my_list = []

with open("task7.1.txt", "r", encoding="utf-8") as file:
    for line in file:
        number = profit(line)
        my_list.append(number)
    aver = 0
    count = 0
    for itm in my_list:
        if itm > 0:
            aver += itm
            count += 1
    aver = aver / count
    my_list1 = [{"firm1": my_list[0], "firm2": my_list[1], "firm3": my_list[2]}, {"average_profit": aver}]

with open("file.json", "w", encoding="utf-8") as file:
    json.dump(my_list1, file)

print("end")