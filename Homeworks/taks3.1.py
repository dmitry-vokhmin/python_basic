def sorting_bubble(list):
    for idx in range(len(list) - 1):
        for itm in range(len(list) - 1):
            if list[itm] < list[itm + 1]:
                list[itm], list[itm + 1] = list[itm + 1], list[itm]
    return list

my_list = sorting_bubble([0, 5, 8, 4, 9, 3])
print(my_list)

def separate(list):
    my_list = []
    for i in range(len(list)):
        my_list.extend(list[i:i + 1])
    list.clear()
    for itm in range(0, len(my_list) - 1, 2):
        if my_list[itm] > my_list[itm + 1]:
            my_list[itm], my_list[itm + 1] = my_list[itm + 1], my_list[itm]
            list.append(my_list[itm: itm + 2])
        else:
            list.append(my_list[itm: itm + 2])
    while len(list) != 1:
        list.append(sorting_merge(list[0], list[1]))
        list.pop(0)
        list.pop(0)
    return list

def sorting_merge(itr, other_itr):
    my_list = []
    count = 0
    other_count = 0
    while count - len(itr) and other_count - len(other_itr):
        if itr[count] < other_itr[other_count]:
            my_list.append(itr[count])
            count += 1
        else:
            my_list.append(other_itr[other_count])
            other_count += 1
    my_list.extend(other_itr[other_count:] if count > other_count else itr[count:])
    return my_list


my_list = separate([2100, 23, 40, 24, 2, 1, 5, 1111, 22])
print(my_list)

def quicksort(list):
    p = list[len(list) // 2]
    count_l = 0
    count_r = -1
    while True:
        if list[count_l] < p:
            count_l += 1
        elif list[count_l] > p:
            if list[count_r] > p:
                count_r -= 1
            elif list[count_r] < p:
                if list[count_l] >= list[count_r]:
                    list[count_l], list[count_r] = list[count_r], list[count_l]
        else:
            break
    a = list[:list.index(p)]
    if len(a) > 2:
        quicksort(a)
    b = list[list.index(p):]
    if len(b) > 2:
        quicksort(b)
    return a, b

my_list = quicksort([4, 9, 7, 6, 2, 3, 8, 0, 1, 19, 10])
print(my_list)