# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import mod_for_hw05_normal
import os
#a = input('1. Перейти в папку\n2. Просмотреть содержимое текущей папки\n3. Удалить папку\n4. Создать папку\n5 - выход\nВыберите:')
a = 'x'
while a != '5':
    # os.system('clear') # очистка экрана(только для Linux) НЕ РАБОТАЕТ
    #clear = lambda: os.system('clear') # ТОЖЕ НЕ РАБОТАЕТ
    #clear
    print('1. Перейти в папку\n2. Просмотреть содержимое текущей папки\n3. Удалить папку\n4. Создать папку\n5 - выход\n')
    a = input('Выберите: ')
    if a == '1':
        dir_path = input('Введите путь: ')
        mod_for_hw05_normal.dir_ch(dir_path) #применяем функцию смены папки из моего модуля
    elif a == '2':
        #dir_path = input('Введите путь: ')
        mod_for_hw05_normal.dir_ls()
    elif a == '3':
        dir_path = input('Введите путь: ')
        mod_for_hw05_normal.dir_rm(dir_path)
    elif a == '4':
        dir_path = input('Введите путь: ')
        mod_for_hw05_normal.dir_mk(dir_path)
    elif a == '5':
        pass
    else: print('Такого выбра нет !')
