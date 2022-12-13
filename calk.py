from math import factorial, sqrt

msg_0 = "Введите арифметическое выражение для подсчета: "
msg_1 = ['Вы знаете, что такое арифметические операции?',
         "Вы вообще знаете, что такое цифры? Будьте внимательны!"]
msg_2 = "Даа ... интересная арифметическая операция. Вы проспали весь школьный курс по математике, не так ли?"
msg_3 = "Мдаа ... деление на 0. Умный шаг..."
msg_4 = "Хотите добавить в память результат вычисления? (y / n):"
msg_5 = "Хотите продолжить вычисления? (y / n):"
msg_6 = " ... ленивы"
msg_7 = " ... очень ленивы"
msg_8 = " ... очень очень ленивы"
msg_9 = "Вы"
msg_10 = "Вы уверены? Здесь только одна цифра! (y / n)"
msg_11 = "Не глупите! Это же только одна цифра! Добавить ее в memory? (y / n)"
msg_12 = "Последний шанс! Вы действительно хотите добавить ее в memory? (y / n)"
msg_ = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]


def is_one_digit(v):
    if -10 < float(v) < 10 and float(v).is_integer():
        return True
    return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (float(v1) == 1 or float(v2) == 1) and v3 == '*':
        msg = msg + msg_7
    if (float(v1) == 0 or float(v2) == 0) and v3 in '*+-':
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
    print(msg)


def read_input(txt):
    my_oper = [b for b in txt if b in '+-/*^√!'][0]
    sp = [c for c in txt.split(my_oper) if c]
    return my_oper, sp


def add(x1, y1):
    return x1 + y1


def dif(x2, y2):
    return x2 - y2


def mult(x3, y3):
    return x3 * y3


def div(x4, y4):
    return x4 / y4


def my_pow(x5, y5):
    return pow(x5, y5)


def my_factor(x6):
    return factorial(int(x6))


def my_sqrt(x7):
    return sqrt(x7)


operations = {
    '+': add,
    '-': dif,
    '*': mult,
    '/': div,
    '^': my_pow,
    '√': my_sqrt,
    '!': my_factor
}

flag = 0
memory = 0
while not flag:

    # обработка исключений
    try:
        oper, inn = read_input(input(msg_0))
        inn = list(map(float, inn))
        # чтение данных из memory
        if inn[0] == 'M':
            inn[0] = memory
        elif len(inn) > 1 and inn[1] == 'M':
            inn[1] = memory
        result = operations[oper](*inn)
    except IndexError:
        print(msg_1[0])
    except (IndexError, ValueError):
        print(msg_1[1])
    except ZeroDivisionError:
        flag = 0
        print(msg_3)
    else:
        flag = 1
        print(result)

    flag2 = 0
    while flag2 == 0 and flag == 1:
        print(msg_4)
        answer = input()
        if answer == 'y':
            if is_one_digit(result):
                msg_index = 10
                flag4 = 0
                while flag4 == 0:
                    print(msg_[msg_index])
                    answer = input()
                    if answer == 'y':
                        if msg_index < 12:
                            msg_index = msg_index + 1
                        else:
                            flag4 = 1
                            memory = result
                    elif answer == 'n':
                        flag4 = 1
                    else:
                        flag4 = 0
                flag2 = 1
            else:
                memory = result
                flag2 = 1
        elif answer == 'n':
            flag2 = 1
        else:
            flag2 = 0
    flag3 = 0
    while flag3 == 0 and flag2 == 1 and flag == 1:
        print(msg_5)
        answer = input()
        if answer == 'y':
            flag = 0
        elif answer == 'n':
            flag3 = 1
        else:
            flag3 = 0
