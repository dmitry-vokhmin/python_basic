from itertools import count, cycle

list1 = [1, 2, 3, 4, 5]
a = 0

for el in count():
    if el > 10:
        break
    print(el)

for el in cycle(list1):
    if a > 10:
        break
    print(el)
    a += 1