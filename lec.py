# # print('Hello world')
# a = 123
# b = 1.23
# value = None
# s = 'Hi'
# f = True

# # вывод строки
# # print(type(a))
# # print(type(b))
# # print(type(value))
# # print(s)

# print(a, ' - ',b, '-', s)
# print(f'{a} - {b} - {s}')
# print(f)

# list = [1,2,'3', 'Hi', True]
# print(list)

# print('Введите а')
# a = float(input())
# print('Введите b')
# b = float(input())
# print(a,b)
# print('{} {}'.format(a,b))
# print(f'{a} {b}')

# print(a, '+', b, '=', a+b)

# a = 1.3123343
# b = 3
# c = round(a * b, 7)
# print(c)

# a = 3
# a *= 5
# print(a)

# funk = 1
# t = 4
# x = 2

# f = [1,2,3,4]
# print(f)
# print(2 in f)

# is_odd = not f[0] % 2
# print(is_odd)

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(f'максимальное число {a}')
# else:
#     print(f'максимальное число {b}')

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)

# for i in range(1, 10, 2):
#     print(i)

# for i in 'qwerty':
#     print(i)


# text = 'съешь ещё этих мягких французских булок'

# help(text.istitle)

# print(len(text))
# print('ещё' in text)
# print(text.isdigit())
# print(text.islower())
# print(text.replace('ещё', 'ЕЩЁ'))
# print(text[0])
# print(text[-5])
# print(text[:])
# print(text[0:5])
# print(text[::6])

# numbers = [1,2,3,4,5]
# print(numbers)

# ran = range(1,6)
# print(type(ran))
# numbers = list(ran)
# print(type(numbers))
# print(numbers)

# numbers[0] = 10
# print(f'{len(numbers)} len')
# print(numbers)

# for i in numbers:
#     i*=2
#     print(i)
# print(numbers)

# numbers.append(6)
# print(numbers)

# numbers.remove(2)
# print(numbers)

# del numbers[2]
# print(numbers)

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

# arg = 2
# print(f(arg))
# print(type(f(arg)))

