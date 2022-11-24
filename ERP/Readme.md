# Задача к уроку № 8: 
## Создать информационную систему для работы с какой либо предметной областью.
Обязательные требования:
1. Разбиение на модули.
2. Внешнее хранилище информации (или БД или файл формата txt / json / csv)
3. Функционал по просмотру, поиску, добавлению, редактированию, удалению информации.

Плюсами будет наличие ГУИ и/или наличие настоящей БД (SQLite3 / PostgreSQL)

## Архитектура информационной системы управления базой данных сотрудников предприятия:
### ! [Архитектура](https://github.com/MamaevEA/Lesson-Python/blob/main/ERP/Arh.jpg)

## Состав команды:
1. Евгений Буслейко. Team-lead. Задачи: модуль - База данных, общее руководство.
2. Евгений Мамаев. Задачи: Модуль - интерфейс.
3. Андрей Панкратов. Задачи: Модуль - добавление, удаление, редактирование сотрудников.
4. Илья Козлов. Задачи: Модуль - Отчетности.

## Описание модулей:
### Интерфейс меню.

Интерфейс меню состоит из следующих блоков:
! [Главное меню "menu()"](https://github.com/MamaevEA/Lesson-Python/blob/main/ERP/Menu.png)
! [Экрана ввода ФИО, даты рождения, телефона и оклада нового сотрудника "vvod()"](https://github.com/MamaevEA/Lesson-Python/blob/main/ERP/Vvod.png)