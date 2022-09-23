# 1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

def InputNum(inputText):
    is_Ok = False
    while not is_Ok:
        try:
            number = int(input(f'{inputText}'))
            is_Ok = True
        except ValueError:
            print('Введено не число!')
    return number

def ChekNum(num):
    if 0 < num < 6:
        print(f'{num} - не является выходным')
    elif 5 < num < 8:
        print(f'{num} - является выходным') 
    else: print('Введено некорректное число')

num = InputNum('Введите номер недели: ')
ChekNum(num)