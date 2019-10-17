SQL_CREATE_NEW_TASK = '''
    INSERT INTO task (title, planned, description) VALUES (?, ?, ?)
'''

SQL_UPDATE_TASK = '''
    UPDATE task SET
        title=?, planned=?, description=?
    WHERE id=?
'''

SQL_UPDATE_TASK_STATUS = '''
    UPDATE task SET done=? WHERE id=?
'''

SQL_SELECT_ALL_TASKS = '''
    SELECT
        id, title, planned, description, done, created
    FROM
        task
'''


SQL_SELECT_TASK_BY_ID = f'{SQL_SELECT_ALL_TASKS} WHERE id=?'

SQL_SELECT_TASKS_PER_DATE = f'{SQL_SELECT_ALL_TASKS} WHERE planned=?'


def initialize(conn, creation_schema):
    """Инициализирует структуру базы данных"""
    with open(creation_schema) as f:
        conn.executescript(f.read())


def create_task(conn, title, planned, description):
    """Сохраняет новую задачу в БД и возвращает ее."""
    cursor = conn.execute(SQL_CREATE_NEW_TASK, (title, planned, description))
    pk = cursor.lastrowid # последний сгенерированный первичный ключ
    conn.commit()
    return get_task(conn, pk)


def update_task(conn, pk, title, planned, description):
    """Обновляет задачу с указанным идентификатором в БД."""
    conn.execute(SQL_UPDATE_TASK, (title, planned, description, pk))


def get_task(conn, pk):
    """
    Выбирает и возвращает из БД задачу с указанным уникальный идентификатором.
    """
    cursor = conn.execute(SQL_SELECT_TASK_BY_ID, (pk,))
    return cursor.fetchone()






