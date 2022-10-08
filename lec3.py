# # Лямбды

# # def f(x):
# #     x**2

# # g = f
# # print(type(f))
# # print(f(1))
# # print(g(1))

# def f(x):
#     return x**2
# g = f
# # print(f(2))
# # print(type(f))
# # print(type(g))
# # print(f(4))
# # print(g(4))

# def calc1(x):
#     return x+10

# # print(calc1(10))

# def calc2(x):
#     return x*10

# # print(calc2(10))

# def math(op, x):
#     print(op(x))

# math(calc2, 10)
# math(calc1, 10)

# def sum(x,y):
#     return x+y

# sum = lambda x, y: x+y

# def mult(x,y):
#     return x*y

# def calc(op, a, b):
#     print(op(a,b))
#     # return op(a,b)

# calc(sum, 4, 5)
# calc(lambda x, y: x+y+1, 4, 5)

# Быстрое создание списков

# list = []

# for i in range(1, 101):
#     # if (i%2 == 0):
#     list.append(i)

# print(list)

# list = [i for i in range(1, 21) if (i%2 == 0)]
# print(list)

# def f(x):
#     return x**3

# list = [(i, f(i)) for i in range(1, 21) if (i%2 == 0)]
# print(list)

# Задача: В файле хранятся числа, нужно выбрать четные и составить список пар
# (число, квадрат числа).
# Пример:
# 1 2 3 5 8 15 23 38
# Получить:
# [(2,4), (8,64), (38,1444)]

# path = 'file2.txt'
# f = open(path, 'r')
# data = f.read() + ' '
# f.close

# numbers = []

# while data != '':
#     spase_pos = data.index(' ')
#     numbers.append(int(data[:spase_pos]))
#     data = data[spase_pos+1:]

# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e**2))
# print(out)

# def select(f,col):
#     return[f(x) for x in col]

# def where(f,col):
#     return[x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()

# res = select(int, data)
# res = where(lambda x: not x%2, res)
# res = select(lambda x: (x, x**2), res)
# print(res)


# MAP
# li = [x for x in range(1,20)]
# li = list(map(lambda x: x +10, li))
# print(li)

# data = list(map(int, input().split()))
# print(data)


# def where(f,col):
#     return[x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()

# res = map(int, data)
# res = where(lambda x: not x%2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)


# Filter

# data = [x for x in range(10)]

# res = list(filter(lambda x: not x%2, data))
# print(res)


# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = filter(lambda x: not x%2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)


# ZIP

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5,9,14,7]
# salary = [111,222,333]

# data = list(zip(users,ids,salary))
# print(data)


# ENUMERATE

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5,9,14,7]
# salary = [111,222,333]

# data = list(enumerate(users))
# print(data)


# СЕМИНАР 07.10.22

# В архиве выкладывают решение домашек. Скачать и дополнить!

# 1. В файле находится N натуральных чисел, записанных через пробел.
#    Среди чисел не хватает одного, чтобы выполнялось условие
#    A[i] - 1 = A[i-1]. Найдите это число. 

# Задача и условие не совпадают! Херня какая-то...

# from random import choice

# def fill_list(count: int):
#     my_list = [x for x in range(count + 1)]
#     my_list.remove(choice(my_list))
#     return my_list

# new_list = (fill_list(int(input('Write count: '))))
# print(new_list)

# def find(my_list: list):
#     for i in range(1, len(my_list)):
#         if my_list[i] - 1 != my_list[i-1]:
#             return my_list[i] - 1
#     return -1

# print(find(new_list))


# 2. Дан список чисел. Создайте список, в который попадают числа,
#    описываемые возрастающую последовательность.
#    Порядок элементов менять нельзя.

# from random import choices

# def new_list (size):
#     list_of_numbers = choices(range(1, size * 2), k = size)
#     return list_of_numbers
# n_list = new_list(10)
# print(n_list)

# def range_nums (new_list: list):
#     my_list = []
#     for i in range(len(new_list)):
#         f = new_list[i] 
#         lis_1 = [f]
#         for x in range(i + 1, len(new_list)):
#             if new_list[x] > f:                
#                 f = new_list[x]
#                 lis_1.append(f)
#         if len(lis_1) > 1:
#             my_list.append(lis_1)
#     return my_list

# print(range_nums(n_list))


# Задание 1 - через сэмпл. Добавляем уникальные строки, сборка набора строк.

# Задание 2 - RLE сжатие. 2 файла - Где взять информацию и куда записать.
# https://fb.ru/article/369240/algoritm-rle-opisanie-osobennosti-pravila-i-primeryi
# Модули для решения задачи: from itertools import groupby, starmap
# from os import path  и exists

# Задача 3. Поле 3 на 3. Без бота. Человек-человек. Исходное поле есть. 
# Некорректные варианты все предусмотреть. 
# https://unicode-table.com/ru/emoji/

# Задача 4. 
# https://informatika.shkolkovo.net/catalog/igry/prostejshie-igry-poisk-vyigryshnoj-strategii


