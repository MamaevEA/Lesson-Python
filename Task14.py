# Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

from random import uniform

def num_in_list(count):
    my_list = list()
    if count < 0:
        return "Error"
    for i in range(count):
        num = round(uniform(1, 10), 2)
        my_list.append(num)
    print(f'Список: ', my_list)
    min = 1
    max = 0
    dif = 0
    for i in range(count):
        if (my_list[i] % 1) < min:
            min = round((my_list[i] % 1), 2)
        if (my_list[i] % 1) > max:
            max = round((my_list[i] % 1), 2)
    dif = round(max - min, 2)
    print(f'Min:', min, 'Max:', max, 'Difference:', dif)

print('Введите чило: ')
num_in_list(int(input()))