from functools import reduce

def sum (prev_el, el):
    return prev_el + el

list1 = [el for el in range(100, 1001) if el % 2 == 0]

print(reduce(sum, list1))
