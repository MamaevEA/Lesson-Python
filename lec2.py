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

