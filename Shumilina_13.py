# ДЗ на понедельник:
# 1. Если в функцию передаётся кортеж, то посчитать длину всех его строк.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Строка – кол-во букв.
# Сделать проверку со всеми этими случаями.
# Использовать готовые типы данных, с клавиатуры ничего не вводится
# Например function([1,2,3,'a','bc8?']) -> 4 числа, 3 буквы
# function((1,2,3,'a','bc8?',7,8,9)) -> 5 символов
# function(788) -> 1
# function('788') -> 0

# 2. Привяжите к предыдущей функции декоратор, который будет выводить информацию о том,
# какой тип данных вы отправили: кортеж, список, число, строку или какой-то другой


def decorator(function):
    def wrapper(arg):
        print('Тип данных:', type(arg), end=' -> ')
        return function(arg)

    return wrapper


@decorator
def tuple_count(tpl):
    return f'длина всех строк - {sum([len(x) for x in tpl if isinstance(x, str)])}'


@decorator
def list_count(lst):
    sp1 = []
    for x in lst:
        sp1.extend(list(str(x)))
    chars = len([y for y in sp1 if y.isalpha()])
    numbers = len([z for z in sp1 if z.isdigit()])
    return f'букв - {chars} и чисел - {numbers}'


@decorator
def number_count(num):
    num = str(num).strip('-').replace('.', '')
    return f'нечетных цифр - {len([x for x in num if int(x) % 2])}'


@decorator
def str_count(line):
    return f'{len([x for x in line if x.isalpha()])} букв'


@decorator
def empty(args):
    return 'для этого типа данных операции не определены'


counts = {
    tuple: tuple_count,
    list: list_count,
    int | float: number_count,
    str: str_count
}

inn = [(1, 2, 3435, 'a', 'bc8?', 7, '8t', 9, 'aj;outwith56', '464gdn+04'),
       [1, 2, 3, 'a', 'bc8?', 'z{P[0RnzFJ]*', 468486, 'm8NWZYyU2S4.'],
       -1341718.8147,
       '7dht-js8862989dsg24xc',
       {},
       (-4) ** 0.5,
       {2, 3}
       ]

print()
for j in inn:
    if isinstance(j, str):
        print(f"'{j}'", end=' -> ')
    elif isinstance(j, complex):
        print('{:.0g}'.format(j), end=' -> ')
    else:
        print(f'{j}', end=' -> ')

    print(counts.get(type(j), empty)(j))
