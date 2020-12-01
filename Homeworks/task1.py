"""
На вход функции подается строка из символов
Резульатт работы функции сжатая строка где указан символ и количество его последовательного повторения
Если символ единичен число 1 записывать не надо
В случае если встречается символ числа во входной строке возбудить ошибку ValueError
"""

def cripto_two(text: str) -> str:
    result = text[0]
    amount = 1
    for idx, char in enumerate(text):
        if char.isdigit():
            raise ValueError('Digit in text')
        if char == result[-1]:
            amount += 1
        else:
            result += f"{amount if amount > 1 else ''}{char}"
    else:
        if amount > 1:
            result += str(amount)
    return result

if __name__ == '__main__':
    texts = {
        1: ('AAABBBEDDQQ', 'A3B3ED2Q2'),
        2: ('Z', 'Z'),
        3: ('DDZUETTCCCCABC', 'D2ZUET2C4ABC'),
    }

    for key, value in texts.items():
        assert crypto(value[0]) == value[1], f"{key} NOT WORK"
