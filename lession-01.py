# Лекция №1

"""
Многострочный
комментарий
"""

"""
todo: Как объявить переменную в Python?

PEP-8
"""
is_debug = True
name = 'Linus'
print(name)


"""
todo: Какие типы данных есть в Python?

1. Скалярные (простые): bool int float complex str bytes
2. Ссылочные (структурные): tuple list set dict object
3. Специальный: None

Все типы данных в Python делятся на:
1. Не изменяемые (immutable): скалярные + tuple
2. Изменяемые (mutable): ссылочные, кроме tuple
"""

"""
todo: Логический тип (bool)
"""
is_student = True
is_admin = False

"""
todo: Целочисленный тип (int)
"""
a = 123
b = -123
c = 0b101010
d = 0o755
e = 0xAF2
f = 0xaf2

"""
todo: Числа с плавающей точкой (float)
"""
f1 = 12.3
f2 = -12.3
f3 = 1e6    # 1 * 10 ^ 6   => 1000000.0
f4 = 12e-3  # 12 * 10 ^ -3 => 0.012


"""
todo: Комплексные числа (complex)
a + bi
i - мнимая единица, i^2 = -1
"""

c1 = complex(2, 3) # => 2+3j
c1.real # => a
c1.imag # => b
c1.conjugate() # => сопряженное комлексное число

c2 = 2+3j
c3 = 3.14j # => 0 + 3.14j


"""
todo: Строки
"""

s1 = 'Hello'
s2 = "Python"
s3 = '""\''
s4 = '''String ' String '''
s5 = """
String
    "
        String
"""
print(s5)

s6 = r'^\d+$' # сырая строка
s7 = u'' # Python2


"""
todo: Байтовая строка (bytes) (Python3)
"""

b1 = b'Hello' # ASCII string
b2 = bytes('Привет', 'utf-8')



"""
todo: Кортеж (tuple)
(1,)
"""

t1 = (1, 2, 3, 1.2, False, '', ("", 3.14j))
print(t1[3], t1[6][1])
# t1[4] = True


"""
todo: Списки (list)
"""
l1 = [1, 2, [], True, ('', '')]
l1[3] = False
print(l1[3])


"""
todo: Множества
"""

set1 = {9, 9, 8, 8, 7, 7}
set1.add(1)
set1.update({666, 1, 8})
print(set1)

set2 = set() # пустое множество


"""
todo: Словари (dict)
"""

d1 = {} # пустой словарь

d2 = {
    'name': 'Linus',
    'skills': ('C++', 'Linux'),
}

print(d2['name'], d2['skills'][1])



var = None


"""
todo: Как определить тип данных переменной в Python?
"""

print(type(d2), type(var), type(s1))


"""
todo: Как выполнить явное приведение переменной
      к определенному типу данных в Python?
"""

print(bool(s1), bool(d1))


"""
todo: Какие операторы существуют в Python?
Арифметические:  + - * / % ** //
Сравнения:       == != > < >= <=
Присваивания:    = += -= *= /= %= **= //=
Побитовые:       & | ~ ^ << >>
Логические:      and or not
Принадлежности:  in, not in
Тождественности: is, not is (для ссылочных типов)
"""
