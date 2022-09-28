# ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

import random

def InputNum(inputText):
    is_Ok = False
    while not is_Ok:
        try:
            number = int(input(f'{inputText}'))
            is_Ok = True
        except ValueError:
            print('Введено не число!')
    return number

def Shuffle(n):
    j = n
    n = range(0,n)
    n = list(n)
    print(f'Список: ', n)
    i = 0
    while i < j:
        x = random.randint(0,j-1)
        n.remove(x)
        n.append(x)
        i = i + 1
    print(f'Перемешанный список: ', n)

num = InputNum('Введите количество элементов (N): ')
Shuffle(num)