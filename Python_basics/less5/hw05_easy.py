# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

##1
import os
i=1
while i < 10:
    os.mkdir(f'dir_{i}')
    i += 1
print(os.listdir()) ## любуемся на результат
##2
import os
i=1
while i < 10:
    os.rmdir(f'dir_{i}')
    i += 1
print(os.listdir())

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
import os

for i in os.listdir(os.getcwd()): # получаем текущий путь, получаем список файлов и папок текущей папки
    if os.path.isdir(i): #если является папкой
        print(i)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import os
import shutil
import sys
file_name = os.path.basename(sys.argv[0]) #из полного пути выделяем только имя файла
shutil.copyfile(sys.argv[0],f'/home/den/{file_name}') # создаём копию файлся с таким же именем