my_list = [7, 5, 3, 3, 2]
i = 0

while True:
    user_num = input("Введите целое число")
    if user_num.isdigit():
        user_num = int(user_num)
        break
    print("Ошибка введено не число")

while True:
    if user_num in my_list:
        ex_ind = my_list.index(user_num)
        my_list.insert(ex_ind, user_num)
        break
    elif user_num > my_list[i]:
        my_list.insert(i, user_num)
        break
    elif i < len(my_list) - 1:
        i += 1
        continue
    else:
        my_list.append(user_num)
        break

print(my_list)