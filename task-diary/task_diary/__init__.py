from textwrap import dedent
import sys
import pkg_resources

from lesson_utils import (
    user_input, multi_line_input, input_datetime, input_int
)

from . import storage
from .services import make_connection


def get_task():
    """Запрашивает идентификатор задачи и возвращает ее из БД"""
    task_id = input_int('Введите ID задачи', required=True)

    with make_connection() as conn:
        task = storage.get_task(conn, task_id)

        if task is None:
            print(f'Задача с "{task_id}" не найдена.')

        return task


def input_task_data(task=None):
    """Запрашивает от пользователя данные о задаче"""
    task = dict(task) if task else {}
    data = {}

    data['title'] = user_input(
        'Название', task.get('title'), required=True
    )

    data['planned'] = input_datetime(
        '%d.%m.%Y %H:%M', 'Запланировано',
        default=task.get('planned'),
        required=True
    )

    data['description'] = multi_line_input(
        'Описание', default=task.get('description')
    )

    return data


def action_list_tasks():
    """Вывести список задач"""


def action_add_task():
    """Добавить задачу"""
    with make_connection() as conn:
        data = input_task_data()
        task = storage.create_task(conn, **data)

    print(f'''Задача "{task['title']}" успешно создана.''')


def action_edit_task():
    """Отредактировать задачу"""
    task = get_task()

    if task is None:
        return

    with make_connection() as conn:
        data = input_task_data(task)
        storage.update_task(conn, task['id'], **data)
        print(f'''Задача "{task['title']}" успешно отредактирована.''')


def action_done_task():
    """Завершить задачу"""


def action_reopen_task():
    """Начать задачу заново"""


def action_show_menu():
    """Показать меню"""
    print(dedent('''
        1. Вывести список задач
        2. Добавить задачу
        3. Отредактировать задачу
        4. Завершить задачу
        5. Начать задачу заново
        m. Показать меню
        q. Выйти
    '''))


def action_exit():
    """Выйти"""
    sys.exit(0)


actions = {
    '1': action_list_tasks,
    '2': action_add_task,
    '3': action_edit_task,
    '4': action_done_task,
    '5': action_reopen_task,
    'm': action_show_menu,
    'q': action_exit,
}

def main():
    with make_connection() as conn:
        schema_path = pkg_resources.resource_filename(__name__, 'resources/schema.sql')
        storage.initialize(conn, schema_path)

    action_show_menu()

    while 1:
        cmd = input('\nВведите команду: ')
        action = actions.get(cmd)

        if action:
            action()
        else:
            print('Не корректная команда')









