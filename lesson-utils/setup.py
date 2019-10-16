"""
name: название пакета
version: версия пакета

description:        Краткое описание
url:                URL - адрес пакета
license:            Лицензия (требуется верная запись)
author:             Имя автора
author_email:       E-Mail автора
packages:           Пакеты, которые нужно скопировать при установке
                    (без рекурсии, необходимо указать вложенные пакеты)
py_modules:         Модули, которые нужно скопировать при установке
scripts:            Запускаемые из командной строки скрипты
instal_requires:    Прямые зависимости пакета от другиз пакетов

"""

from setuptools import setup

setup(
    name='lesson-utils',
    version='0.1.0',
    description='Collection useful features for the course Python',
    license='Appache License 2.0',
    author='capybarralt',
    author_email='capybarralt@gmail.com',
    packages=['lesson_utils'],
    instal_requires=[
        'appdirs',
    ]
)
