"""
todo: Исключения
"""

try:
    a = input()

    if a.isdigit():
        a = int(a)
    else:
        print('Вы ввели не число')

    b = int(input())

    print(a + b)
except ValueError as err:
    print(err)
except TypeError as err:
    print(err)
else:
    print('Выполняется если не было исключений')
finally:
    print('Выполняется всегда')



try:
    int(input()) + input()
except (ValueError, TypeError) as err:
    print(err)

try:
    int(input())
except:
    pass #!!!!!!!!!!!!!!
