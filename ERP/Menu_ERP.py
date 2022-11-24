import easygui
from easygui import *  

def menu(): # Создает интерфейс меню
    global type_vvod
    type_vvod = ''
    output=''
    while output != "Выйти":
        msg = "Информационная система управления базой данных сотрудников компании 'Рога и копыта'"
        title = "Меню"
        choices = ["Принять нового сотрудника", "Уволить сотрудника", \
        "Редактировать данные сотрудника", "Вывести отчет", "Выйти"]
        output = buttonbox(msg, title, choices)

        if output == "Принять нового сотрудника":
            type_vvod = 1
            vvod()
            count = str(calc(var_fin))
            tmp = ''
            tmp = var1 + ' равно ' + count
            easygui.msgbox(tmp)
            save_log(make_answer(var1, count, False))
        elif output == "Посчитаем комплексное число":
            type_vvod = "Комплексное число"
            vvod()
            count = str(Complex_calculator(var_fin))
            tmp = ''
            tmp = var1 + ' равно ' + count
            easygui.msgbox(tmp)
            save_log(make_answer(var1, count, False))
        elif output == "Посмотрим логи":
            viev_log()
        elif output == "Бежим отсюда!":
            exit()
    
def vvod(): # Создает интерфейс окна ввода уравнения
    global var1                 # Переменная куда будем записывать данные.
    msg = "Введите уравнение"   # Сообщение
    title = "Ввод уравнения"    # Шапочка.
    fieldNames = ["Уравнение"]  # Ввод уравнения
    fieldValues = []  
    fieldValues = multenterbox(msg,title, fieldNames)
    var1 = fieldValues[0]       # Запись уравнения в переменную (строка)


menu()

