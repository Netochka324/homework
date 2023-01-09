import sqlite3 as sq

# Создадим БД
with sq.connect('Shumilina.db') as conn:
    # Создаем курсор
    cursor = conn.cursor()  # cursor - указатель на таблицу БД

    # Если таблицы существуют - удаляем их
    # cursor.execute('''DROP TABLE IF EXISTS fio''')
    cursor.execute('''DROP TABLE IF EXISTS animals''')

    # Создадим таблицу в fio БД
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS fio(
            имя TEXT PRIMARY KEY, 
            фамилия TEXT,
            возраст INTEGER
        )
    ''')

    # Заполнение fio
    inn = [
        ('Анна', 'Шумилина', 37),
        ('Светлана', 'Ерошкина', 28),
        ('Степан', 'Перевертев', 30)
    ]

    # cursor.executemany('INSERT INTO fio VALUES(?, ?, ?)', inn)
    for x in inn:
        try:
            cursor.execute('INSERT INTO fio VALUES(?, ?, ?)', x)
        except sq.IntegrityError:
            print(' '.join(map(str, x)), '- данная запись в базе существует и дублироваться не будет')

    # Создадим таблицу animals в БД
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS animals(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT, 
            age INTEGER
        )
    ''')

    # Заполнение animals
    cursor.execute('''INSERT INTO animals(name, age) VALUES('Мулька', 2)''')
    cursor.execute('''INSERT INTO animals(name, age) VALUES('Тошка', 3)''')
    cursor.execute('''INSERT INTO animals(name, age) VALUES('Степан', 1)''')

    # Сохранение изменений в БД
    conn.commit()

    # Вывод содержимого в консоль
    cursor.execute('''SELECT * FROM fio''')
    print('\nFIO: ')
    for rez in cursor:
        print(*rez)
    print('\nAnimals: ')
    cursor.execute('''SELECT * FROM animals''')
    for rez in cursor:
        print(*rez)

