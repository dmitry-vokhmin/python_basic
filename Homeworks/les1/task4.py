user_number = int(input("Введите целое положительное число"))
last_digit = user_number % 10
max_number = 0

while user_number != 0:
    user_number = user_number // 10
    number = user_number % 10
    if number > last_digit:
        max_number = number
else:
    if max_number < last_digit:
        max_number = last_digit

print("Максимальное число " + str(max_number))
