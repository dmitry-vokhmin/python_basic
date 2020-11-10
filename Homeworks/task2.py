file = open("task2.1.txt", "r")
content = file.readlines()

a = len(content)
print(f"Количество строк: {a}")

for idx, el in enumerate(content, 1):
    a = el.count(" ")
    print(f"Количество слов в {idx} строке: {a + 1}")

file.close()