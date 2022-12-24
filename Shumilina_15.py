# На понедельник:
# Класс состоит из двух методов
# 1 метод: принимает либо строку, либо число.
# Если передаю строку: если произведение количества гласных и согласных
# меньше или равно длине строки, то вывести все гласные. Иначе все согласные
# Если передаю число: вывести произведение суммы четных цифр на длину числа.
# Использовать len в 1 методе нельзя, вместо len используйте второй метод.
# 2 метод: возвращает длину строки или числа. Можно использовать len
# obj = Class
# obj.method1('abc') # -> a
# obj.method1(987)# -> 24

class MyClass:

    def method1(self, inn):
        if type(inn) == str:
            gl = ''.join([x for x in inn if x in 'aeouieyаоуыэе'])
            sogl = ''.join([y for y in inn if y.isalpha() and y not in gl])
            if self.my_len(gl)*self.my_len(sogl) <= self.my_len(inn):
                print(gl)
            else:
                print(sogl)
        elif type(inn) in (int, float):
            inn_str = str(inn).replace('-', '').replace('.', '')
            sum_even_numbers = sum([int(x) for x in inn_str if not int(x) % 2])
            print(sum_even_numbers * self.my_len(inn))
        else:
            print(f'Для типа данных {type(inn)} действий не предусмотрено')

    def my_len(self, inn):
        return len((str(inn)).replace('-', '').replace('.', ''))


obj = MyClass()
obj.method1(-459.123)
obj.method1('aa5')
obj.method1('ababa1b')
obj.method1([1, 2, 3])
obj.method1({1: 3, 2: 0})
