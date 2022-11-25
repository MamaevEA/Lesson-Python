# Задача к уроку № 8: 
## Создать информационную систему для работы с какой либо предметной областью.
Обязательные требования:
1. Разбиение на модули.
2. Внешнее хранилище информации (или БД или файл формата txt / json / csv)
3. Функционал по просмотру, поиску, добавлению, редактированию, удалению информации.

Плюсами будет наличие ГУИ и/или наличие настоящей БД (SQLite3 / PostgreSQL)

## Архитектура информационной системы управления базой данных сотрудников предприятия:
### ![Архитектура](https://github.com/MamaevEA/Lesson-Python/blob/main/ERP/Arh.png)

## Состав команды:
1. Евгений Мамаев. Задачи: Модуль - интерфейс, добавление, удаление сотрудников, база данных, общее руководство.
2. Андрей Панкратов. Задачи: Модуль - редактирование данных сотрудников.
3. Илья Козлов. Задачи: Модуль - отчетности.

## Описание модулей.
### Интерфейс меню.

![Главное меню "menu()"](https://github.com/MamaevEA/Lesson-Python/blob/main/ERP/Menu.png)
Главное меню "menu()"
---
![Окно ввода ФИО, даты рождения, телефона и оклада нового сотрудника "vvod()"](https://github.com/MamaevEA/Lesson-Python/blob/main/ERP/Vvod.png)
Окно ввода ФИО, даты рождения, телефона и оклада нового сотрудника "vvod()"
---
![Окно выбора пола, вводимого сотрудника "Sex"](https://github.com/MamaevEA/Lesson-Python/blob/main/ERP/Sex.png)
Окно выбора пола, вводимого сотрудника "Sex"
---
![Окно выбора должности, вводимого сотрудника "Job_title"](https://github.com/MamaevEA/Lesson-Python/blob/main/ERP/Job_title.png)
Окно выбора должности, вводимого сотрудника "Job_title"
---
![Окно выбора подразделения, вводимого сотрудника "Subdvision"](https://github.com/MamaevEA/Lesson-Python/blob/main/ERP/Subdivision.png)
Окно выбора подразделения, вводимого сотрудника "Subdvision"
---
![Окно ввода табельного номера, удаляемого сотрудника "Dell"](https://github.com/MamaevEA/Lesson-Python/blob/main/ERP/Dell.png)
Окно ввода табельного номера, удаляемого сотрудника "Dell"
---
![Окно ввода табельного номера, редактируемого сотрудника "Edit"](https://github.com/MamaevEA/Lesson-Python/blob/main/ERP/Edit.png)
Окно ввода табельного номера, редактируемого сотрудника "Edit"
---
![Окно выбора редактируемого параметра](https://github.com/MamaevEA/Lesson-Python/blob/main/ERP/Edit_Change.png)
Окно выбора редактируемого параметра
---
![Окно ввода нового имени](https://github.com/MamaevEA/Lesson-Python/blob/b979c8df7bdfc3fd5548c666d7b9737c932fb4c5/ERP/Edit_Name.png)
Окно ввода нового имени
---
![Окно ввода нового дня рождения](https://github.com/MamaevEA/Lesson-Python/blob/85f7134e970ff0f91be43f3dfe64d9a5e9017900/ERP/Edit_Day.png)
Окно ввода нового дня рождения
---
![Окно ввода нового месяца рождения](https://github.com/MamaevEA/Lesson-Python/blob/85f7134e970ff0f91be43f3dfe64d9a5e9017900/ERP/Edit_Month.png)
Окно ввода нового месяца рождения
---
![Окно ввода нового года рождения](https://github.com/MamaevEA/Lesson-Python/blob/85f7134e970ff0f91be43f3dfe64d9a5e9017900/ERP/Edit_Year.png)
Окно ввода нового года рождения
---
![Окно ввода нового пола](https://github.com/MamaevEA/Lesson-Python/blob/85f7134e970ff0f91be43f3dfe64d9a5e9017900/ERP/Edit_Sex.png)
Окно ввода нового пола
---
![Окно ввода новой должности](https://github.com/MamaevEA/Lesson-Python/blob/85f7134e970ff0f91be43f3dfe64d9a5e9017900/ERP/Edit_Job_title.png)
Окно ввода новой должности
---
![Окно ввода нового подразделения](https://github.com/MamaevEA/Lesson-Python/blob/85f7134e970ff0f91be43f3dfe64d9a5e9017900/ERP/Edit_Subdivision.png)
Окно ввода нового подразделения
---
![Окно ввода нового телефона](https://github.com/MamaevEA/Lesson-Python/blob/85f7134e970ff0f91be43f3dfe64d9a5e9017900/ERP/Edit_Phone.png)
Окно ввода нового телефона
---
![Окно ввода нового оклада](https://github.com/MamaevEA/Lesson-Python/blob/85f7134e970ff0f91be43f3dfe64d9a5e9017900/ERP/Edit_Salary.png)
Окно ввода нового оклада
---
![Окно выбора вида отчета](https://github.com/MamaevEA/Lesson-Python/blob/85f7134e970ff0f91be43f3dfe64d9a5e9017900/ERP/Search.png)
Окно выбора типа отчета
---
![Окно вывода всех сотрудников](https://github.com/MamaevEA/Lesson-Python/blob/85f7134e970ff0f91be43f3dfe64d9a5e9017900/ERP/Search_all.png)
Окно вывода всех сотрудников
---
![Окно вывода телефонного справочника](https://github.com/MamaevEA/Lesson-Python/blob/85f7134e970ff0f91be43f3dfe64d9a5e9017900/ERP/Searche_Phone.png)
Окно вывода телефонного справочника
---
![Окно выбора параметра отчета](https://github.com/MamaevEA/Lesson-Python/blob/85f7134e970ff0f91be43f3dfe64d9a5e9017900/ERP/Searche_Change.png)
Окно выбора параметра отчета
---
![Окно ввода должности для поиска](https://github.com/MamaevEA/Lesson-Python/blob/85f7134e970ff0f91be43f3dfe64d9a5e9017900/ERP/Search_Job_title.png)
Окно ввода должности для поиска
---
![Окно вывода результатов поиска по должности](https://github.com/MamaevEA/Lesson-Python/blob/85f7134e970ff0f91be43f3dfe64d9a5e9017900/ERP/Rez_Job_title.png)
Окно вывода результатов поиска по должности
---
![Окно ввода года рождения для поиска](https://github.com/MamaevEA/Lesson-Python/blob/85f7134e970ff0f91be43f3dfe64d9a5e9017900/ERP/Search_Year.png)
Окно ввода года рождения для поиска
---
![Окно вывода результатов поиска по году рождения](https://github.com/MamaevEA/Lesson-Python/blob/85f7134e970ff0f91be43f3dfe64d9a5e9017900/ERP/Rez_Year.png)
Окно вывода результатов поиска по году рождения
---
![Окно ввода диапазона зарплат для поиска](https://github.com/MamaevEA/Lesson-Python/blob/85f7134e970ff0f91be43f3dfe64d9a5e9017900/ERP/Search_Salary.png)
Окно ввода диапазона зарплат для поиска
---
![Окно вывода результатов поиска по зарплате](https://github.com/MamaevEA/Lesson-Python/blob/85f7134e970ff0f91be43f3dfe64d9a5e9017900/ERP/Rez_Salary.png)
Окно вывода результатов поиска по зарплате
---