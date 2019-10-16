"""
DRY
"""

from datetime import datetime

__all__ = (
    'user_input', 'input_int', 'input_float', 'confirm', 'multi_line_input'
)


def user_input(msg='Введите значение', default=None, value_callback=None,
               trim_spaces=True, show_default=True, required=False):
    if show_default and default is not None:
        # f-строки для форматирования строки
        msg += f' [{default}]'  # ' [{}]'.format(default)

    if default is not None:
        requiered = False

    while 1:
        value = input(f'{msg}: ')
        if trim_spaces:
            value = value.strip()

        if value:
            if value_callback is None:
                return value
            try:
                return value_callback(value)
            except ValueError as err:
                print(err)

        else:
            if not requiered:
                return default
            print('Требуется внести значение')

def input_int(msg='Введите число', default=None, required=False):
    return user_input(msg, default, value_callback=int, required=required)

def input_int_bin(msg='Введите число', default=None, required=False):
    return user_input(msg, default, value_callback=lambda v: int(v, 2),
                      required=requiered)

def input_float(msg='Введите число', default=None, required=False):
    return user_input(msg, default, value_callback=float, required=required)

#user_input('Введите имя', value_callback=int, required=True)
#input_int()



# Функция задающий вопрос с вариантами ответа
def confirm(msg='Подтвердите дейвствие', default_yes=False, default_no=False,
            required=False):

    def callback(value):
        # если нужно сопоставить значения, то использовать нужно словарь
        answers = {
            'y': True,
            'yes': True,
            'no': False,
            'n': False,
        }

        answer = answers.get(value.lower()) # есть такой ключ - значение; нет - None

        if answer is None:
            valid_values = '/'.join(answers.keys())
            raise ValueError(f'Допустимые значения: {valid_values}')

        return answer

    if default_yes and default_no:
        # Инструкция позволяет прервать штатный поток исполнения при
        # помощи возбуждения исключения
        raise RuntimeError('Аргумента default_no и default_yes заданы как True')

    if default_yes:
        default = True
        msg += ' [Y/n]'
    elif default_no:
        default = False
        msg += ' [y/N]'
    else:
        default = None
        msg += ' [y/n]'

    return user_input(msg, default, value_callback=callback, show_default=False,
                      required=required)

#print(confirm())

# Функция осуществляющая многострочный ввод
def multi_line_input(msg='Введите текст', default=None):
    print('Ctrl+D/Ctrl+Z (Windows) для завершения ввода')
    print(f'{msg}')

    if default is not None:
        print('[Оставьте поле пустым, чтоб использовать значение по умолчанию]')

    text = []

    while 1:
        try:
            value = input('> ')
            if not text and not value:
                return default

            text.append(value)
        except EOFError:
            print('\n')
            return '\n'.join(text)

def input_datetime(fmt, msg='Введите дату: ', default=None, required=False):
    if default is not None:
        default = datetime.strptime(fmt, default)

    return user_input(
        msg, default, required=required,
        value_callback=lambda value: datetime.strptime(value, fmt)
    )

def input_date(mt, msg='Введите дату: ', default=None, required=Fals):
    value = input_datetime(fmt, msg, default, required=required)

    if value is None:
        return value

    return value.date()

#print(__name__)
# Выполняется только если файл исполняемый, а не импортированный модуль
if __name__ == '__main__':
    print(multi_line_input())
