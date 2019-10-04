"""
TODO: Модули

Вайл с раширением .ру это модуль
имя модуля - это его индитификатор для испльзования
Как ищет модули?
Сначала ищет в рабочей директории, а затеи в PYTHONPATH
каждый модуль создает свое пространство имен

"""

"""
TODO: как импориторвать модули?

"""

# # todo: 1. Импорт модуля целиком
#
# import sys
# import input_utils
#
# print(sys.path)
#
# a = input_utils.input_int()
#
#
# # todo: 2. Частичный import
#
# from input_utils import input_float, input_int_bin
# b = input_float()
# c = input_int_bin()
#
#
# # todo: 3. Импорт со *
# # все что не перечислено в __all__ по звехдочке не перекинет
# from input_utils import *
#
#
# # todo: Как задать псевдоним?
#
# from input_utils import user_input as base_user_input
# import os.path as path


# import demo
#
# print(demo.is_debug())           # получилиFalse
# demo.debug = True
# print(demo.is_debug())           # получилиTrue


# from demo import debug, is_debug
#
# print(is_debug())                  # получили False
# debug = True
# print(is_debug())                  # Получили False


# from demo import lst, get
#
# lst.append(1) # ссылка
# print(get())
#
# lst = [1, 2, 3] # другой список
# print(get())


"""
TODO: Главный (исполняемый) модуль

"""
