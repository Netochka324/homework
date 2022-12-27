# ДЗ на четверг:
# Класс Company:
# Создайте класс Company
class Company:
    # Создайте статическое свойство levels, которое будет содержать (как словарь) все уровни квалификации программиста:
    # 1:junior, 2:middle, 3:senior, 4:lead.
    _levels = {1: 'junior', 2: 'middle', 3: 'senior', 4: 'lead'}

    # Создайте метод __init__(), внутри которого будут определены два protected свойства:
    # 1) _index - передается параметром и
    # 2) _levels - принимает из словаря levels значение с ключом _index
    def __init__(self, _index):
        self._index = _index
        self._levels = self._levels[_index]

    # Создайте метод _level_up(), который будет переводить программиста на следующий уровень
    def _level_up(self):
        if self._index <= 2:
            self._index += 1

    # Создайте метод is_lead(), который будет проверять, что программист достиг последней квалификации
    def is_lead(self):
        return self._index == 3


# Класс Programmer(Company):
# Создайте класс Programmer
class Programmer(Company):
    default_level = Company._levels[0]

    # Создайте метод __init__(), внутри которого будут определены 3 динамических свойства:
    # 1) name - передается параметром, является публичным,
    # 2)age - возраст
    # 3) level – уровень квалификации на основе словаря из Company
    def __init__(self, name, age, index, level=default_level):
        # super().__init__(_levels)
        super().__init__(index)
        self.name = name
        self.age = age
        self.level = input('''Введите уровень квалификации сотрудника:
        1: 'junior', 
        2: 'middle', 
        3: 'senior', 
        4: 'lead' ''')

    # Создайте метод work(), который заставляет программиста работать, что позволяет ему становиться более
    # квалифицированным с помощью метода _level_up() родительского класса
    def work(self):
        if not self.is_lead():
            Company.
        else:
            print('Уровень сотрудника достиг максимального!')

    # Создайте мeтод info(), который выведет
    # информацию о вас: имя, возраст, квалификацию
    def info(self):
        print(f'''Имя: {self.name}
        Возраст: {self.age}
        Квалификация: {self.level}''')
# Создайте статический метод knowledge_base(), который выведет в консоль справку по программированию
# (просто любой текст).
