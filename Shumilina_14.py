print('Task1')


def upper(func):
    def wrapper(name):
        val = func(name.upper())
        return val

    return wrapper


@upper
def privet(name):
    return 'Привет, % s!' % name


print(privet(input('Введите имя: ')))

print('Task2')


def my_sum(num):
    razr = len(str(num)) - 1
    if num > 0:
        return num // (10 ** razr) + my_sum(num % (10 ** razr))
    else:
        return 0


print('Сумма цифр числа -', my_sum(int(input('Введите число: '))))
