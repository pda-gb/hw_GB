# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    number = (number * (10 ** ndigits) + 0.44) // 1
    number = number / (10 ** ndigits)
    return number


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


##№1
def lucky_ticket(ticket_number):
    i = 0
    a = 0
    len_str = 0
    list_ticket = []
    answer = ('Счастливый', 'обычный')

    list_ticket = list(str(ticket_number))
    list_ticket = list(map(int, list_ticket))

    a = len(list_ticket) % 2 ## определение чётности

    itm1 = 0
    itm1 = int(len(list_ticket) / 2) ## длина половины номера билета

    if a == 0 and sum(list_ticket[:itm1]) == sum(list_ticket[:itm1]):
        i = 0
    else: i = 1



    return answer[i]



print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))




