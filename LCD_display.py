a1 = ' -- '
a2 = '    '
a3 = '|   '
a4 = '   |'
a5 = '|  |'
pict = {0: [a1, a5, a5, a2, a5, a5, a1],
        1: [a2, a4, a4, a2, a4, a4, a2],
        2: [a1, a4, a4, a1, a3, a3, a1],
        3: [a1, a4, a4, a1, a4, a4, a1],
        4: [a2, a5, a5, a1, a4, a4, a2],
        5: [a1, a3, a3, a1, a4, a4, a1],
        6: [a1, a3, a3, a1, a5, a5, a1],
        7: [a1, a4, a4, a2, a4, a4, a2],
        8: [a1, a5, a5, a1, a5, a5, a1],
        9: [a1, a5, a5, a1, a4, a4, a1]
        }
numbers = [int(x) for x in list(input())]

if numbers:
    print('x' + '-' * (5 * len(numbers)) + 'x')
    for i in range(7):
        line = ''
        line += '|'
        if i < 6:
            for t in numbers:
                line += pict[t][i] + ' '
        else:
            for t in numbers:
                line += pict[t][i] + ' '
        line += '|'
        print(line)

    print('x' + '-' * (5 * len(numbers)) + 'x')
