# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

def InputNum(inputText):
    is_Ok = False
    while not is_Ok:
        try:
            number = int(input(f'{inputText}'))
            is_Ok = True
        except ValueError:
            print('Введено не число!')
    return number

def SummNum(num):
    l = []
    i=0
    summ = 0
    print(f'Лист: ', end='')
    while i < num:
        l.append((1+(1/(i+1))) ** (i+1))
        l[i] = round(l[i])
        summ = summ + l[i]
        i = i + 1
    print(l)
    print(f'Сумма чисел листа: ', summ)

num = InputNum('Введите число: ')
SummNum(num)
