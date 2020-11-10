file = open("task4.1.txt", "r")

content = file.readline()
russian_1 = content.replace("one", "один")

content = file.readline()
russian_2 = content.replace("two", "два")

content = file.readline()
russian_3 = content.replace("three", "три")

content = file.readline()
russian_4 = content.replace("four", "четыре")
file.close()

file = open("task4.2.txt", "w", encoding='utf-8')
str_list = [russian_1, russian_2, russian_3, russian_4]
file.writelines(str_list)
file.close()