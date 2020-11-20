number = 18
count = 1
block = 0
param = 1
floor = 0
if number == 1:
    floor = 1
    position = 1
else:
    while block == 0:
        if number in range(1, (count**2 + param)):
            block = count
            floor += 1
        else:
            param = count**2 + param
            floor += count
            count += 1
    if (number - (param - 1)) % block == 0:
        floor = floor + ((number - (param - 1)) // block) - 1
        position = ((number - param) % block) + 1
    else:
        floor = floor + ((number - (param - 1)) // block)
        position = (number - (param - 1)) % block

print(f"{floor} этаж")
print(f"{position} позиция")