# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def InputNum(inputText):
    is_Ok = False
    while not is_Ok:
        try:
            number = float(input(f'{inputText}'))
            is_Ok = True
        except ValueError:
            print('Введено не число!')
    return number

def SummNum(num):
    num = num * (10 ** len(str(num)))
    summ = 0
    while num > 0:
        summ = summ + (num % 10)
        num = num // 10
    print(f'Сумма чисел равно: ', summ)

num = InputNum('Введите число: ')
if num >= 0:
    SummNum(num)
else: 
    num = num * -1
    SummNum(num)

