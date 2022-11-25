import logger as log

import simple_calc as simple

import print_log as prin

import coplex as compl



print(              'Меню')
print()
print ('1. Вычисление вещественных чисел')
print  ('2. Вычисление комплексных чисел')
print('3. Печать логов')
print('4. Выход')
print()
sum=''
choice=int(input('Введите ваш выбор 1-4: '))
if (choice==1) or (choice==2):
    sum=input('Введите пример в одну строку (комплексные числа должны быть в скобках): ')
    if (choice == 1):
        result=simple.calculation(sum)
    else:
        result=compl.calculation(sum)
    # text = '2+2'
    # digital = (2 + 3j)
    answer_in_string = log.make_answer(sum, result, False)
    log.save_log(answer_in_string)

elif (choice==3):
    prin.viev_log()
else: print('Желаю всего хорошего!')
