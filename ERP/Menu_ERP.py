import easygui
from easygui import *  
import json
import random


def menu(): # Создает интерфейс меню
    global type_vvod        # Переменная, куда записывается выбор пользователя
    type_vvod = ''
    output=''
    while output != "Выйти":        # Пока не будет выбрана кнопка "Выйти", меню будет возобновляться
        msg = "Информационная система управления базой данных сотрудников компании 'Рога и копыта'"
        title = "Меню"
        choices = ["Принять нового сотрудника", "Уволить сотрудника", \
        "Редактировать данные сотрудника", "Вывести отчет", "Выйти"]
        output = buttonbox(msg, title, choices)
        if output == "Принять нового сотрудника":
            type_vvod = 1
            vvod()
            new_people()
        elif output == "Уволить сотрудника":
            type_vvod = 2
            dell()
        elif output == "Редактировать данные сотрудника":
            type_vvod = 3
            edit()
        elif output == "Вывести отчет":
            report()
        elif output == "Выйти!":
            exit()
    
def vvod(): # Создает интерфейс ввода нового сотрудника
    global var1                 # Переменная куда будем записывать ФИО, Дату рождения, Телефон и Оклад.
    global sex                  # Переменная, куда записывают пол сотрудника.
    global job_title            # Переменная, куда записывают должность сотрудника.
    global subdivision          # Переменная, куда записывают подразделение сотрудника
    msg = "Введите данные сотрудника"   # Сообщение
    title = "Ввод нового сотрудника"    # Шапочка.
    fieldNames = ["Фамилия, Имя, Отчество", "День рождения (дд)", "Месяц рождения (мм)", \
        "Год рождения (гггг)", "Телефон", "Оклад"]
    fieldValues = []  
    fieldValues = multenterbox(msg,title, fieldNames)
    var1 = fieldValues      # Запись данных в переменную в виде листа
    
    fieldValues = []            # Следующее окно интерфейса выбора пола
    title = "Выбор пола"
    msg = var1[0]
    fieldNames = ["Мужской", "Женский"] # Сюда можно добавить словарь
    fieldValues = buttonbox(msg,title, fieldNames)
    sex = fieldValues           # Данные о поле записаны в переменную sex

    fieldValues = []            # Следующее окно интерфейса выбора должности
    title = "Выбор должности"
    msg = var1[0]
    fieldNames = ["Директор", "Начальник отдела", "Менеджер по продажам", "Инженер", \
        "Бухгалтер", "Уборщик"] # Сюда можно добавить словарь
    fieldValues = choicebox(msg,title, fieldNames)
    job_title = fieldValues     # Данные о должности записаны в переменную job_title

    fieldValues = []            # Следующее окно интерфейса выбора подразделения
    title = "Выбор подразделения"
    msg = var1[0]
    fieldNames = ["Администрация", "Отдел продаж", "ИТ-отдел", "АХО"] # Сюда можно добавить словарь
    fieldValues = choicebox(msg,title, fieldNames)
    subdivision = fieldValues     # Данные о подразделении записаны в переменную subdivision

def dell():
    global dell_human       # Переменная, куда записывается ID сотрудника, которого надо удалить
    msg = "Введите табельный номер сотрудника, которого хотите удалить из базы данных"   # Сообщение
    title = "Удаление сотрудника"    # Шапочка.
    fieldNames = ["Табельный номер"]  # Ввод ID
    fieldValues = []  
    fieldValues = multenterbox(msg,title, fieldNames)
    dell_human = fieldValues      # Запись ID удаляемого сотрудника в переменную dell_human


def edit():             
    global edit_human    # Переменная, куда записывается ID сотрудника, которого надо отредактировать
    msg = "Введите табельный номер сотрудника, данные которого хотите откорректировать"   # Сообщение
    title = "Редактирование данных сотрудника"    # Шапочка.
    fieldNames = ["Табельный номер"]  # Ввод ID
    fieldValues = []  
    fieldValues = multenterbox(msg,title, fieldNames)
    edit_human = fieldValues      # Запись ID корректируемого сотрудника в переменную edit_human

def report():
        global type_report
        msg = "По какому признаку вы хотите сформировать отчет?"
        title = "Отчеты"
        choices = ["По должности", "По году рождения", \
        "По диапазону зарплат", "А можно всех посмотреть? ;)"]
        output = buttonbox(msg, title, choices)
        
        if output == "По должности":
            fieldValues = []            # Следующее окно интерфейса выбора должности
            title = "Выбор должности"
            fieldNames = ["Директор", "Начальник отдела", "Менеджер по продажам", "Инженер", \
                    "Бухгалтер", "Уборщик"] # Сюда можно добавить словарь
            fieldValues = choicebox(msg,title, fieldNames)
            type_report = fieldValues     # Данные о должности записаны в переменную type_report
        
        elif output == "По году рождения": # Следующее окно интерфейса ввода года
            title = "Ввод года рождения"    
            fieldNames = ["Год рождения"]  
            fieldValues = []  
            fieldValues = multenterbox(msg,title, fieldNames)
            type_report = fieldValues      # Запись года рождения в переменную type_report
        
        elif output == "По диапазону зарплат": # Следующее окно ввода диапазона зарплат
            title = "Ввод диапазона зарплат"    
            fieldNames = ["Минимум", "Максимум"]  
            fieldValues = []  
            fieldValues = multenterbox(msg,title, fieldNames)
            type_report = fieldValues      # Запись диапазона зарплат в переменную type_report
        elif output == "А можно всех посмотреть? ;)":
            type_report = "All"     
            # При выводе всех сотрудников, в переменную type_report записывается строка "All".

def uniqueid():
    seed = random.getrandbits(32)
    while True:
       yield seed
       seed += 1

def new_people():
        unique_sequence = uniqueid()
        ID = next(unique_sequence)
        dob = [int(var1[1]), int(var1[2]), int(var1[3])]
        data = {}
        data[ID] = []
        data[ID].append({
            'Name': str(var1[0]),
            'Sex': str(sex),
            'Day of Birth': dob,
            'Phone': var1[4],
            'Salary': var1[5],
            'Job_title': str(job_title),
            'Subdivision': str(subdivision) 
        })

        with open('ERP/data.txt', 'a') as outfile:
            json.dump(data, outfile, indent=2, ensure_ascii=False)

menu()
print(var1)
