# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000

def transformation_num(count):
    if count < 0:
        return "Error"
    num = 0
    res = 0
    while count > 0:
            for i in range(count):
                num = (count % 2) * 10**i
                res += num
                count //= 2
    print(f'Двоичное число: ', res)

print('Введите чило: ')
transformation_num(int(input()))
