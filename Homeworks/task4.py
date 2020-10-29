user_input = input("Введите строку из нескольких слов через пробел")
string = user_input.split()

for i in range(len(string)):
    if len(string[i]) > 10:
        print(i + 1, ")", string[i][:10])
        continue
    print(i + 1, ")", string[i])

