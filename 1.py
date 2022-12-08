print('\nЗадача №2.')

print('Проверка ввода двух чисел: ValueError и ZeroDivisionError')
while 1:
    try:
        num1 = int(input('Введите первое число: '))
    except ValueError:
        print('Это не число! Введите число заново.')
    else:
        print('Первое число принято.')
        break

while 1:
    try:
        num2 = int(input('Введите второе число: '))
    except ValueError:
        print('это не число!')
    else:
        try:
            c = num1 / num2
        except ZeroDivisionError:
            print('Деление на ноль! Введите число заново.')
        else:
            print('Второе число принято.')
            break

print('\nПроверка на ValueError:')
try:
    a, b = input('Введите число: ')
except ValueError:
    print('Ошибка - неверное количество значений')
else: print('a =', a, 'b =', b)

print('\nПроверка на TypeError, IndexError:')
from random import choice

s = input('Введите два числа списка через пробел:').split()
print('список:', s)
try:
    num1 += choice(s)
except TypeError:
    print('Ошибка типа! Действие отменено.')
else:
    while 1:
        try:
            n = int(input('Введите индекс элемента списка - 0 или 1: '))
            print(s[n])
        except ValueError:
            print('Это не число! Введите число заново.')
        except IndexError:
            print('Ошибка - индекс за границей диапазона!')
        else:
            print('Индекс принят.')
            break

print('\nПроверка на ModuleNotFoundError:')
try:
    import randint

    num = randint(0, 10)
    print(num)
except ModuleNotFoundError:
    print('Ошибка - не импортирован модуль!')

print('\nПроверка на SyntaxError:')
print('Создадим SyntaxError в нашем моделе my_module1 и импортируем его:')
try:
    # генерируем SyntaxError в модуле my_module1
    import my_module1
except SyntaxError:
    print('Ошибка - в модуле!')
else:
    print('Ошибок нет')

print('\nПроверка на NameError:')
try:
    somename += 1
except NameError:
    print('Ошибка - переменная с таким именем не найдена!')
# rghuhrhvjhgjgjj
# посадил дед брюкву