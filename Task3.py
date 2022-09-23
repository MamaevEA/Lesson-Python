# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

def InputNum(inputText):
    is_Ok = False
    while not is_Ok:
        try:
            number = int(input(f'{inputText}'))
            is_Ok = True
        except ValueError:
            print('Введено не число!')
    return number

def CheckPosition(x,y):
    if x > 0 and y > 0:
        print(f'Точка с координатами X = {x}, Y = {y} находится в первой четверти')
    elif x < 0 and y > 0:
        print(f'Точка с координатами X = {x}, Y = {y} находится во второй четверти')
    elif x < 0 and y < 0:
        print(f'Точка с координатами X = {x}, Y = {y} находится в третьей четверти')
    elif x > 0 and y < 0:
        print(f'Точка с координатами X = {x}, Y = {y} находится в четвертой четверти')
    elif x == 0 or y == 0:
        print(f'Ошибка: нельзя воодить координаты X или Y равные 0') 

x = InputNum('Введите координату Х: ')
y = InputNum('Введите координату Y: ')

CheckPosition(x,y) 