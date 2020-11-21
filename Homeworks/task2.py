number = 15
count = 1
param = 1
floor = 0

while number not in range(1, (count**2 + param)):
        param = count**2 + param
        floor += count
        count += 1
if (number - (param - 1)) % count == 0:
    floor = floor + ((number - (param - 1)) // count)
    position = ((number - param) % count) + 1
else:
    floor = floor + ((number - (param - 1)) // count) + 1
    position = (number - (param - 1)) % count

print(param)
print(count)
print(f"{floor} этаж")
print(f"{position} позиция")