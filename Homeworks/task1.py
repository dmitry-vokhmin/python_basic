def text():
    my_list = []
    while True:
        user_input = input("Введите строку, для выхода нажмите enter")
        if user_input == "":
            break
        my_list.append(user_input + "\n")
    return my_list

file = open("task1.1.txt", "w")
file.writelines(text())
file.close()