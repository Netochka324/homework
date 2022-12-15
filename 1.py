# while 1:
#     try:
#         num1 = int(input('Введите первое число: '))
#     except ValueError:
#         print('Это не число! Введите число заново.')
#     else:
#         print('Первое число принято.')
#         break
#
# while 1:
#     try:
#         num2 = int(input('Введите второе число: '))
#     except ValueError:
#         print('это не число!')
#     else:
#         try:
#             c = num1 / num2
#         except ZeroDivisionError:
#             print('Деление на ноль! Введите число заново.')
#         else:
#             print('Второе число принято.')
#             break
#
# s = [-5, 'g']
# try:
#     from random import choice
#     num1 = choice(s)
# except TypeError as t:
#     print('Ошибка -', t)
# else:
#     while 1:
#         try:
#             n = int(input('Введите индекс элемента списка - 0 или 1: '))
#             print(s[n])
#         except ValueError:
#             print('Это не число! Введите число заново.')
#         except IndexError:
#             print('Ошибка - индекс за границей диапазона!')
#         else:
#             print('Индекс принят.')
#             break
#
# try:
#     import randint
#     num1 = num1+s.randint(0, 2)
# except ModuleNotFoundError:
#     print('Ошибка - не импортирован модуль!')
# except IndentationError:
#     print('Ошибка - проверьте синтаксис!')

from math import factorial, sqrt


def read_input(txt):
    oper = [x for x in txt if x in '+-/*^√!'][0]
    sp = [float(x) for x in txt.split(oper) if x]
    return oper, sp


def add(x, y):
    return x + y


def dif(x, y):
    return x - y


def mult(x, y):
    return x * y


def div(x, y):
    return x / y


def my_pow(x, y):
    return pow(x, y)


def my_factor(x):
    return factorial(x)


def my_sqrt(x):
    return sqrt(x)


operations = {
    '+': add,
    '-': dif,
    '*': mult,
    '/': div,
    '^': my_pow,
    '√': my_sqrt,
    '!': my_factor
}

calc = input()
oper, inn = read_input(calc)
s = operations[oper](*inn)
print(f'{s:.2f}')
