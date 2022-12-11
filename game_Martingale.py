from random import choice

colors = ['red', 'black']

while True:
    Q = input('Введите начальную сумму: ')
    if Q.isdigit():
        Q = int(Q)
        break
while True:
    color = input("Введите на какой цвет ставите: %s/%s " % (colors[0], colors[1]))
    if color in colors:
        break
while True:
    my_stavka = input('Введите начальную ставку: ')
    if my_stavka.isdigit():
        my_stavka = int(my_stavka)
        my_stavka0 = my_stavka
        break

Q -= my_stavka

i = 0
while Q > 0:
    i += 1
    print('У вас на счету: %d единиц. Вы сделали ставку %d на «%s»' % (Q, my_stavka, color))
    ruletka = choice(colors)
    if ruletka == color:
        print('Вы выиграли %d!' % (my_stavka*2))
        Q += 2*my_stavka
        my_stavka = my_stavka0
        Q -= my_stavka
    else:
        print('Вы проиграли %d!' % my_stavka)
        my_stavka *= 2
        Q -= my_stavka

print('''\nВы проиграли! Количество ставок - %d.
Стратегия не работает, иначе игра продолжалась бы бесконечно :)''' % i)
