# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4

# out
# [2, 5, 8, 10]
# [20, 40]

from random import sample

def num_in_list(count):
    if count < 0:
        return "Error"
    my_list = sample(range(1, 10), count)
    print(f'Список: ', my_list)
    new_list = list()
    for i in range(count//2):
        gen = my_list[i] * my_list[(i+1)*-1]
        new_list.append(gen)
    print(f'Произведение пар чисел', new_list)

print(f'Задайте количество элементов списка:')
num_in_list(int(input()))