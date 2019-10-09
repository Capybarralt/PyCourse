"""
Базы данных

SQLite3 - базы данных в файле

SQL:
    DDL
    DML - манипулирование данными

Алгортим взаимодействия с БД
1. Соединение с свервером БД
    1.1. Опционально (для СУБД), выбрать базу данных
2. Выполнение запросов
    2.1. Получить объект курсор (опционально)
    2.2. Выполнить завпрос с помощью метода execute() объекта курсор
    2.3. Если запрос на изменнеие стурктуры БД или данных:
        2.3.1. Нужно зафиксировать изменения (опционально)
    2.4. Если запрос на получение данных (SELECT):
        2.4.1. Фактические данные нужно раз-fetch-ить:
            - fetchall()   - получить все строки таблицы в список
            - fetchclone() - получить одну строку таблицы
            - fetchmany(N) - получить N строк из таблицы в список

connect(detect_types)
Какие значения допустимы для detect_types:
    PARSE_DECLTYPES - анализировать объявленный тип для каждого возвращаемого
                      столбца.
    PARSE_COLNAMES - анализировать имя столбца
        id [int] INTEGER

"""

import sqlite3

sql = '''
    CREATE TABLE IF NOT EXISTS task (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        title TEXT NOT NULL,
        description TEXT NOT NULL DEFAULT '',
        planned TIMESTAMP NOT NULL,
        done BOOLEAN NOT NULL DEFAULT 0,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
'''

sql_insert = '''
    INSERT INTO task (title, planned, description) VALUES (?, ?, ?)
'''

sql_select = '''
    SELECT
        id, title, planned, description, done, created
    FROM
        task
'''

sql_update = '''
    UPDATE task SET
        title=?, planned=?, description=?
    WHERE
        id=?
'''

sql_delete = '''
    DELETE FROM tasks WHERE id=?
'''

# conn = sqlite3.connect('db.sqlite') # утсановка соединения
#
# cursor = conn.cursor() # получаем объект курсор
# cursor.execute(sql) # выполнение запроса
# conn.commit() # фиксируем изменения
#
# conn.close() # закрываем соединение

# контексный менеджер автоматически вызывает commit и close
with sqlite3.connect('db.sqlite', detect_types=sqlite3.PARSE_DECLTYPES) as conn:
    conn.row_factory = sqlite3.Row

    conn.execute(sql) # создает курсор, а затем вызывает execute()

    conn.execute(sql_insert, ('Сделать ДЗ', '2019-10-10 00:00:00', 'Срочно'))

    cursor = conn.execute(sql_select)
    tasks = cursor.fetchall()
    print(tasks)

    for task in tasks:
        print(f'{task["title"]} {type(task["planned"])}')
