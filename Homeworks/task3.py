def maximum(list):
    max_number = list[0]
    for el in list:
        if el > max_number:
            max_number = el
    return max_number

def my_func(a, b, c):
    my_list = [a, b, c]
    max1 = maximum(my_list)
    my_list.remove(max1)
    max2 = maximum(my_list)
    return max1 + max2

c = my_func(1, 2, 3)
print(c)


