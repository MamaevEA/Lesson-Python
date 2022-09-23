# 5. Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

import math

def InputNum(inputText):
    is_Ok = False
    while not is_Ok:
        try:
            number = int(input(f'{inputText}'))
            is_Ok = True
        except ValueError:
            print('Введено не число!')
    return number

def Distans(x,y):
    print(f'Расстояние между точками = {math.sqrt(((y[0]-x[0])**2) + ((y[1]-x[1])**2))}')


x1 = InputNum('Введите координату Х первой точки: ')
y1 = InputNum('Введите координату Y первой точки: ')
x2 = InputNum('Введите координату Х второй точки: ')
y2 = InputNum('Введите координату Y второй точки: ')

a = [x1,y1]
b = [x2,y2]

Distans(a,b)