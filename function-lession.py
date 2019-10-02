"""
TODO: Функции

Одна функция выполняет сугубо одну задачу
Давать говорящее название - желательно глагол
можно на время создать пустую функцию, если указать внутрии нее pass
"""

def say_hello():
    print('Hello-say')

"""
 TODO: Выполнение
"""

say_hello()

"""
TODO: Возвращение значения
"""

def get_hello():
    return 'Hello-get' #работает только внутри функции. Может быть и пустым.
                       #Мгновенно завершает функцию
result = get_hello()
print(result)

"""
TODO: Как передать аргумент
"""

def print_greeting(username):
    print('Hello,', username, '!')

print_greeting('Vlad')

def multi(a, b):
    return a*b

print(multi(5, 4))

"""
TODO: Как задать значение аргумента по умолчанию
"""

def my_pow(x, p = 2):
    return x**p

print(my_pow(2))    # 2^2
print(my_pow(2,3))  # 2^3

"""
TODO: Позиционные и именованные аргументы
Можно не соблюдать порядок аргумнтов, если использовать их имена
"""

print(my_pow(p=5, x=7)) #

"""
TODO: Переменное количество аргументов
"""

def multi_cool(a, b, *numbers): # numbers будет кортежем
    print(type(numbers), numbers)
    result = a * b
    for i in numbers:
        result *= i
    print(result)

multi_cool(1, 2)
multi_cool(1, 2, 3)

def db_connect(provider, **options): # любое количестов именнованых компонетов
    print('Connecting to database:', provider)
    print('===>', type(options), options)

db_connect('sqlite', filename='db.sqlite')
db_connect('mysql', host='localhost', user='root', port=666)

"""
TODO: Как развернуть кортеж, список в значения позиционных аргументов
"""

lst = [8, 20]
print(multi(*lst))

lst = range(1,10)
print(multi_cool(*lst))

"""
TODO: Развернуть словарь
"""

config = {
    'provider': 'mysql',
    'host':'dfs',
    'user': 'Vlad',
    'pswd': 'toor'
}

db_connect(**config)

"""
TODO: Явное различие аргументов в Python3, во втором рабоать не будет
"""

def demo_arguments(a, b=None, *с, d, e=None, **f):
    print(a, b, c, d, e, f)
# a - обязательный, a и b позициоооные, c не обязательный, к d и e только
#по имени, f - обяазтельно именованный, после * все только именованные.

"""
TODO: Передача значений аргументов по ссылке
"""

def split_pieces(s, size, output=None):
    if output is None:
        output = []
    start = 0
    end = len(s)
    while start < end:
        output.append(s[start:start+size])
        start += size
    return output


found = []
split_pieces('hello, my name Vladislav', 4, found)
print(found) # изменился без присовения

found2 = split_pieces('hello, my name Vladislav', 4)
print(found2)


def demo_defaults(x, lst=[]):
    print(lst)
    lst.append(x**2)
    print(lst)

demo_defaults(2)
demo_defaults(3)
# Список будет расти. Старые данные остались.
# Нельзя передавать изменяемые типы данных. Передавать None по умолчанию

 """
 TODO: Анонимные Функции
 Callback - функция обратного вызова, функция в одну строку
 Не очень хорошо класть в переменную. Лямда функция яавтоматически возвращает значение
 """

sqrt = lambda x: x ** .5
print(sqrt(9))

 """
 TODO: Рекурсивная функция
 Функция, которая вызыввет саму себя
 Рекурсия есть прямая и косвенная. а вызывает б, а б вызывает а. Из них нужно
 выйти - косвенная
 """

def factorial(n):
    return 1 if n ==0 else n * factorial(n-1)

print(factorial(5))

"""
TODO: Замыкание
"""
# обрезает с начала и конца нужные символы.
def trim(chars=None):
    # Замкнутая область видимости
    print(chars)

    def f(s):
        return s.strip(chars)
        # не объявляем nonlocal. Так как мы не меняем, а считываем. Питон пойдет ее искать выше.
        # для изменяемых типов данных nonlocal тоже не нужен, так как рабоат идет с сылками
    return f # возвращаем ссылку на функцию.

trim_spaces = trim()
trim_slashes = trim('/|\\')
print(trim_spaces, trim_spaces('     123    '))
print(trim_slashes, trim_slashes('//||1|2//'))

"""
TODO: Область видимости
глобальная
локальная - все что находится в теле функции
"""

g = 666

def f():
    external = 777

    def func():
        # без этой строки функция не увидет глобальную переменнную и выдаст ошибку
        global g
        # не сможет найти без этой строки. Будет искать в локальных родительских функциях. Только в Python3
        nonlocal external
        g += 1
        external += 1

    func()
    print(g, external)

f()
# Глобальные переменнные зло!!!
