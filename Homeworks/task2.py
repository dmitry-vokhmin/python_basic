list1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [el for idx, el in enumerate(list1[1:]) if list1[idx] < el]
print(result)