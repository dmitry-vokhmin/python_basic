def elevator(number):
    count = 1  # блок
    param = 1  # номер первой комнаты в блоке
    floor = 1  # Этаж блока

    # number >= (param + count ** 2)

    while number >= (param + count ** 2):
        param = count ** 2 + param
        floor += count
        count += 1

    floor, position = floor + ((number - param) // count), number - (((number - param) // count) * count + param) + 1

    return floor, position


if __name__ == '__main__':
    a = elevator(10**20)
    print(a)