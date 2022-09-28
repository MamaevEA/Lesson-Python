# Напишите программу, которая принимает на вход 2 числа. 
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15

def InputNum(inputText):
    is_Ok = False
    while not is_Ok:
        try:
            number = int(input(f'{inputText}'))
            is_Ok = True
        except ValueError:
            print('Введено не число!')
    return number

def Summa(x,y,z):
    l = range(-x,x+1)
    l = list(l)
    summ = l[y-1] * l[z-1]
    print(f'Список элементов:')
    print(l)
    print(f'Произведение цифр под номерами: ', y, 'и', z, 'равно', summ)
        
num = InputNum('Введите количество элементов (N): ')

pos1 = InputNum('Введите первое число: ')
while (((num*2) + 1) < pos1) or (pos1 < 1):
    print('Первое число находиться за пределами диапазона')
    pos1 = InputNum('Введите первое число: ')

pos2 = InputNum('Введите второе число: ')
while (((num*2) + 1) < pos2) or (pos1 < 1):        
    print('Второе число находиться за пределами диапазона')
    pos2 = InputNum('Введите второе число: ') 

Summa(num,pos1,pos2)