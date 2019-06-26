# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

var_list = ["яблоко", "банан", "киви", "арбуз"]
i = 0
while i < len(var_list):
    print(i+1, '.', '{:>7}'.format(var_list[i]))
    i += 1
## не пойму, почему на выходе,между цифрой и точкой. получается пробел



# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

# enter 1 list
a = input('len1')
len_list1 = int(a)
var_list1 = []
i = 0
while i< len_list1:
    var_list1.append(input())
    i += 1

# enter 2 list
a = input('len2')
len_list2 = int(a)
var_list2 = []
i = 0
while i< len_list2:
    var_list2.append(input())
    i += 1

# delete double
set1 = set(var_list1)
set2 = set(var_list2)
print(set1 - set2)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

import random
# enter 1 list
a = input('len1')
len_list1 = int(a)
var_list1 = []
var_list2 = []
i = 0
while i < len_list1:
    var_list1.append(random.randint(0, 100))
    i += 1
print(var_list1)

for itm in var_list1:
    if itm % 2 == 0:
        var_list2.append(itm / 4)
    else: var_list2.append(itm * 2)
print(var_list2)