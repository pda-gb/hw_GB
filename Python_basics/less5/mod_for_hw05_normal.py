def dir_mk(str_path):  ## создаём папку
    import os
    if os.access(f'{str_path}', os.F_OK) is False:  # проверяем существование объекта
        if os.access(os.path.dirname(f'{str_path}'), os.W_OK):  # проверяем права на запись объекта вмсте где создаётся обьект(os.path.dirname)
            os.mkdir(f'{str_path}')
            print('Вы создали папку:\n', os.listdir())
        else: print('Нет прав доступа!')
    else: print('Файл или папка уже существует!')
    return None


def dir_rm(str_path):  ## удаляем папку со всем содержимым
    import os
    import shutil
    if os.access(f'{str_path}', os.F_OK):  # проверяем существование объекта
        if os.access(f'{str_path}', os.W_OK):  # проверяем права на запись объекта
            shutil.rmtree(f'{str_path}')
            print('Успешно удалено')
        else: print('Нет прав доступа!')
    else: print('Файла или папки не существует!')
    return None


def dir_ls(): ## функция показывет содержимое папки
    import os
    i = []
    if os.access(os.getcwd(), os.F_OK):  # проверяем существование объекта
        if os.access(os.getcwd(), os.R_OK):  # проверяем права на чтение объекта
            print('Содержимое:\n')
            for i in os.listdir(os.getcwd()):  # получаем текущий путь, получаем список файлов и папок текущей папки
                print(i)
        else: print('Нет прав доступа!')
    else: print('Файла или папки не существует!')
    return None


def dir_ch(str_path): # функция - перейти в папку
    import os
    if os.access(f'{str_path}', os.F_OK):  # проверяем существование объекта
        if os.access(f'{str_path}', os.R_OK):  # проверяем права на чтение объекта
            os.chdir(str_path)
            print('Вы в папке:\n', os.getcwd())
        else: print('Нет прав доступа!')
    else: print('Файла или папки не существует!')
    return None


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
#import os
#import shutil
#import sys

#file_name = os.path.basename(sys.argv[0])  # из полного пути выделяем только имя файла
#shutil.copyfile(sys.argv[0], f'/home/den/{file_name}')  # создаём копию файлся с таким же именем
