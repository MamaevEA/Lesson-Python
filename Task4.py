# 4. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y). 

def InputNum(inputText):
    is_Ok = False
    while not is_Ok:
        try:
            number = int(input(f'{inputText}'))
            is_Ok = True
        except ValueError:
            print('Введено не число!')
    return number

def CheckPosition(x):
    if x == 1:
        print(f'Диапазон возможных координат течек в первой четверти: \n 0 : X : +∞ \n 0 : Y : +∞')
    elif x == 2:
        print(f'Диапазон возможных координат течек во второй четверти: \n -∞ : X : 0 \n 0 : Y : +∞')
    elif x == 3:
        print(f'Диапазон возможных координат течек в третьей четверти: \n -∞ : X : 0 \n -∞ : Y : 0') 
    elif x == 4:
        print(f'Диапазон возможных координат течек в четвертой четверти: \n 0 : X : +∞ \n -∞ : Y : 0')
    else:
        print(f'\nВведен некорректный номер четверти: {x}')
        x = InputNum('Введите корректный номер четверти (от 1 до 4): ')
        CheckPosition(x)

x = InputNum('Введите номер четверти: ')
CheckPosition(x)
