# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21

def fibonachi (count):
    my_list = list()
    my_list.append(1)
    my_list.append(0)
    my_list.append(1)
    if count < 0:
        return "Error"
    elif count == 1:
        print(my_list)
    else:
        i = 3
        while i < (count * 2):
            f1 = my_list[i-1] + my_list[i-2]
            my_list.append(f1)
            if len(my_list) % 4 == 0:
                f2 = my_list[i] * -1
            else:
                f2 = my_list[i]
            my_list.insert(0, f2)
            i += 2
        print('Список чисел Фибоначи: ')
        print(my_list)

print('Введите чило: ')
fibonachi(int(input()))