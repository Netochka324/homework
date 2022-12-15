# from math import factorial, sqrt
#
# msg_0 = "Введите арифметическое выражение для подсчета: "
# msg_1 = [
#     "Вы знаете, что такое арифметические операции?",
#     "Вы вообще знаете, что такое цифры? Будьте внимательны! Числа должны быть действительными!",
#     "Для факториала и квадратного корня число должно быть также неотрицательным."
# ]
# msg_2 = "Даа ... интересная арифметическая операция. Вы проспали весь школьный курс по математике, не так ли?"
# msg_3 = "Мдаа ... деление на 0. Умный шаг..."
# msg_4 = "Хотите добавить в память результат вычисления?"
# msg_5 = "Хотите продолжить вычисления?"
# msg_6 = " ... могли это сами вычислить"
# msg_7 = " ... точно могли"
# msg_8 = " ... определенно могли."
# msg_9 = "Вы"
# msg_10 = "Вы уверены? Здесь только одна цифра!"
# msg_11 = "Не глупите! Это же только одна цифра! Добавить ее в memory?"
# msg_12 = "Последний шанс! Вы действительно хотите добавить ее в memory?"
# msg_ = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]
#
#
# # проверка цифр до 10
# def is_one_digit(v):
#     if -10 < float(v) < 10 and float(v).is_integer():
#         return True
#     return False
#
#
# # проверка простых вычислений
# def check(v, v3):
#     msg = ""
#     if all(map(lambda x: is_one_digit(float(x)), v)):
#         msg = msg + msg_6
#     if any(map(lambda x: float(x) == 1, v)) and v3 in '*!√^':
#         msg = msg + msg_7
#     if any(map(lambda x: float(x) == 0, v)) and v3 in '*+-':
#         msg = msg + msg_8
#     if msg != "":
#         msg = msg_9 + msg
#     print(msg)
#
#
# # чтение исходных данных для вычисления
# def read_input(txt):
#     my_oper = [b for b in txt if b in '+-/*^√!'][0]
#     sp = [c for c in txt.split(my_oper) if c]
#     return my_oper, sp
#
#
# # функции
# def add(x1, y1):
#     return x1 + y1
#
#
# def dif(x2, y2):
#     return x2 - y2
#
#
# def mult(x3, y3):
#     return x3 * y3
#
#
# def div(x4, y4):
#     return x4 / y4
#
#
# def my_factor(x6):
#     return factorial(int(x6))
#
#
# def my_sqrt(x7):
#     return sqrt(x7)
#
#
# operations = {
#     '+': add,
#     '-': dif,
#     '*': mult,
#     '/': div,
#     '^': pow,
#     '√': my_sqrt,
#     '!': my_factor
# }
#
# flag = 0
# memory = 0
# while not flag:
#     # обработка исключений
#     try:
#         oper, inn = read_input(input(msg_0))
#
#         # чтение данных из memory
#         if inn[0] == 'M':
#             inn[0] = memory
#         elif len(inn) > 1 and inn[1] == 'M':
#             inn[1] = memory
#
#         # проверка на малые значения
#         check(inn, oper)
#
#         inn = list(map(float, inn))
#         result = operations[oper](*inn)
#     except IndexError:
#         print(msg_1[0])
#     except ValueError:
#         if :
#             print(msg_1[1])
#         else:
#             print(msg_1[2])
#     except ZeroDivisionError:
#         print(msg_3)
#     else:
#         flag = 1
#         print(f'{result:.3f}')
#
#         # добавление результата в memory
#         flag2 = 0
#         while not flag2 and flag:
#             print(msg_4)
#             answer = input('(y / n): ')
#
#             if answer == 'y':
#                 if is_one_digit(result):
#                     msg_index = 10
#                     flag4 = 0
#
#                     while not flag4:
#                         print(msg_[msg_index])
#                         answer = input('(y / n): ')
#                         if answer == 'y':
#                             if msg_index < 12:
#                                 msg_index = msg_index + 1
#                             else:
#                                 flag4 = 1
#                                 memory = result
#                         elif answer == 'n':
#                             flag4 = 1
#                 else:
#                     memory = result
#                 flag2 = 1
#             elif answer == 'n':
#                 flag2 = 1
#
#         # запрос на продолжение вычислений
#         flag3 = 0
#         while not flag3 and flag2 and flag:
#             print(msg_5)
#             answer = input('(y / n): ')
#             if answer == 'y':
#                 flag = 0
#             elif answer == 'n':
#                 flag3 = 1
#             else:
#                 flag3 = 0
#
# написать функцию square кот приним 1 аргумент - сторона квадрата, выводит в виде кортежа периметр площадь и диагональ
#
# import calendar
#
# print(calendar.month(2016,5))
#
#
#
# функция простое число
import random

#
# def is_prime(num):
#     s = 0
#     for i in range(2, num):
#         if not num % i:
#             s += 1
#             return False
#     return True
#
#
# print(is_prime(int(input())))
