# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

a_list = [random.randint(0, 10) for _ in range(10)] ##заполняем список десятью случ. целыми числами от 0 до 10
b_list = list(map(lambda x: x*x, a_list))
#b_list = [a_list[i]*a_list[i] for i in a_list] нерабочй вариант
print(a_list, b_list)
# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

a_list = ['q', 'a', 's', 'w', 'd', 'x']
b_list = ['i', 'q', 'b', 'd', 'u', 'y']
i = 0
j = 0
c_list = []
c_list = [a for a in a_list for b in b_list if a == b]  # на каждый элемент a_list перебираются элементы b_list, если
                                                        # они равны, то добавить в список.
print(c_list)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

a_list = [random.randint(-20, 20) for _ in range(50)]
b_list = []
def my_func(x): ## проверяет на положительность числа, кратность трём и не кратность 4 и возвращает True
    a = False
    if x > 0:
        if x % 3 == 0:
            if x % 4 != 0:
                a = True
    else: a = False
    return a

b_list = [i for i in a_list if my_func(i) is True] ##заполняем список генератором из a_list и соответствующих Rtue  через my_func
print(b_list)