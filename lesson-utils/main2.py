"""
Пакеты
Пакет - много модулей (может содержать пакеты)

"""

import lesson_utils

#lesson_utils.input_utils.confirm

from lesson_utils import input_utils

#input_utils.confirm

from lesson_utils.input_utils import confirm

#confirm()


"""
__init__.py

"""

from lesson_utils import input_int # ошибка. В пакете нет модуля input_int
# искать будет в модуле по умолчанию __init__
# Добавим в __init__ from input_utils import *
# Но все равно ругается
# Правильно from lesson_utils.input_utils import *
# Но еще лучше испольщовать относительное расположение
# from .input_utils import *
# относительный импорт нельзя использовать в исполняемом модуле
