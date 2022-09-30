# Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22

from random import sample

def num_in_list(count):
    if count < 0:
        return "Error"
    my_list = sample(range(1, count * 2), count)
    print(f'Список: ', my_list)
    summ = 0
    for i in range(count):
        if i % 2 == 0:
            summ += my_list[i]
    print(f'Сумма элементов на нечетных позициях: ', summ)

print(f'Задайте количество элементов списка:')
num_in_list(int(input()))
