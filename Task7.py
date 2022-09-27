# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def InputNum(inputText):
    is_Ok = False
    while not is_Ok:
        try:
            number = int(input(f'{inputText}'))
            is_Ok = True
        except ValueError:
            print('Введено не число!')
    return number

def ListGen(num):
    i = 1
    n = 1
    while i <= num:
        print(n)
        n= n * (i+1)
        i = i + 1

num = InputNum('Введите число: ')
ListGen(num)