"""
На вход функции подается строка из символов
Резульатт работы функции сжатая строка где указан символ и количество его последовательного повторения
Если символ единичен число 1 записывать не надо
В случае если встречается символ числа во входной строке возбудить ошибку ValueError
"""

def crypto(text: str) -> str:
    result = ""
    amount = 1
    if len(text) > 1:
        try:
            for idx, itm in enumerate(text):
                if text[idx + 1] != itm:
                    result += text[idx]
                if text[idx + 1] == itm:
                    amount += 1
                else:
                    if amount != 1:
                        result += str(amount)
                        amount = 1
                if itm.isdigit():
                    raise ValueError
        except IndexError:
            if itm.isdigit():
                raise ValueError
            if amount != 1:
                result += itm + str(amount)
            else:
                result += itm
    else:
        result += text
    return result

if __name__ == '__main__':
    texts = {
        1: ('AAABBBEDDQQ', 'A3B3ED2Q2'),
        2: ('Z', 'Z'),
        3: ('DDZUETTCCCCABC', 'D2ZUET2C4ABC'),
    }

    for key, value in texts.items():
        assert crypto(value[0]) == value[1], f"{key} NOT WORK"
