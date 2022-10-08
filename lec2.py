# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'w')
# data.writelines(colors)
# data.write('\nLINE \n')
# data.write('LINEEE \n')
# data.close()

# with open('file.txt', 'a') as data:
#     data.write('\nLINE \n')
#     data.write('LINEEE \n') 



# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close

# import lec as l
# print(l.f(1))

# def concatenation(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res

# print(concatenation('a', 'b', 'c', 'd'))
# print(concatenation('a', '1'))

# Кортежи
# a = (3, 4, 7)
# print(a)
# print(a[0])
# print(a[-1])

# for item in a:
#     print(item)

# Словари
# dictionary = {}
# dictionary = \
#     {
#         'up': 'вверх',
#         'left': 'влево',
#         'down': 'вниз',
#         'right': 'вправо'
#     }

# print(dictionary)
# print(dictionary['left'])

# for k in dictionary.keys():
#     print(k)

# for k in dictionary.values():
#     print(k)

# Множества
# colors = {'red', 'green', 'blue'}
# print(colors)
# colors.add('red')
# print(colors)
# colors.add('gray')
# print(colors)
# colors.remove('red')
# print(colors)
# colors.clear()
# print(colors)

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()
# u = a.union(b)
# i = a.intersection(b)
# dl = a.difference(b)
# dr = b.difference(a)

# q = a \
#     .union(b) \
#     .difference(a.intersection(b))

# s = frozenset(a)

# Листы
# list1 = [1,2,3,4,5]

# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop(0))
# print(list1)
# print(list1.insert(2, 11))
# print(list1)
# print(list1.append(5))
# print(list1)

# Задачи на семинаре.
# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#    Напишите программу, которая определит, присутствует ли в заданном списке число,
#    полученное от пользователя.

# from random import sample
# def num_in_list(count, number):
#     if count < 0:
#         return "Error"
#     my_list = sample(range(1, count * 2), count)
#     print(my_list)
#     if number in my_list:
#         return "Yes"
#     return "No"
    
# print(num_in_list(int(input()), int(input())))

# 2. Задайте список, состоящий из произвольных слов, количество задаёт пользователь.
#    Напишите программу, которая определит индекс второго вхождения строки в списке
#    либо сообщит, что её нет.

# from random import choices
# def list_new(n, word):
#     new_list =[]
#     for i in range(n):
#         a=choices(word,k=3)
#         new_list.append(''.join(a))
#     return new_list

# def list_search(my_list, key):
#     if my_list.count(key) >1:
#         print('Yes')
#         n=my_list.index(key)
#         print(my_list.index(key,n+1))
#     else:
#         print(-1)
# result=list_new(20, "abc")
# print(result)
# list_search(result, input())

# 1. Задайте строку из набора чисел. Напишите программу,
#    которая покажет большее и меньшее число.
#    В качестве символа-разделителя используйте пробел.

# Вариант решения 1:
# list_1 = [int(x.strip(',.*')) for x in line.split() if x.replace("-", "").isdigit()]
list_1 = [x.strip(',.*') for x in input().split() if x.replace("-", "").isdigit()]
print(f'Min: {min(list_1, key=int)}')
print(f'Max: {max(list_1, key=int)}')

# Вариант решения 2: 
list_1 = []
for x in input().split():
    if x.replace("-", "").isdigit():
        list_1.append(x.strip(',.*'))
        
print(f'Min: {min(list_1, key=int)}')
print(f'Max: {max(list_1, key=int)}')

# Вариант решения 3:
def check(str_list):
    for i, num in enumerate(str_list):
        str_list[i] = num.strip('.,;:?!')
        if not str_list[i].replace("-", "").isdigit():
            return []
    return str_list


def find_max_min(nums_str: str):
    list_nums = nums_str.split()
    right_list = check(list_nums)

    if right_list:
        return min(right_list, key=int), max(right_list, key=int)
    print("The data is incorrect")
    return []


print(*find_max_min(input("Enter the numbers separated by a space: ")))


# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0,
#    с помощью дополнительных библиотек python. Запросите значения А, В, С 3 раза.
#    Уравнения и корни запишите в файл.

from math import sqrt

def sqr_r(a, b, c):
    d = b ** 2 - 4 * a * c
    if a == 0:
        return 'Error'
    with open('sqr.txt', 'a', encoding='utf-8') as my_f:
        my_f.write(f'{a}x² + {b}x + ({c}) = 0\n')
        if d > 0:
            my_f.write(f'{(-b + sqrt(d)) / (2 * a)}\n')
            my_f.write(f'{(-b - sqrt(d)) / (2 * a)}\n')
        elif d == 0:
            my_f.write(f'{-b / (2 * a)}\n')
        else:
            my_f.write('Нет корней\n')


for i in range(3):
    sqr_r(int(input('A: ')), int(input('B: ')), int(input('C: ')))
    print()

# 3. Задайте два числа. Напишите программу, которая найдёт
#    НОК (наименьшее общее кратное) этих двух чисел.

from math import gcd
a=int(input('a = '))
b=int(input('b = '))
print(a*b//gcd(a,b))
print(gcd(a,b))

# ДЗ 1 - через decimal

# ДА 2 - https://autogear.ru/article/371/831/chislo-prostyih-deliteley-chisla-skolko-deliteley-imeet-prostoe-chislo/

