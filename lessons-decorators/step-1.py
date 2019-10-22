# todo: Шаг 1. Дополняем работу функции, не изменяя оригинальную

def say_hello():
    return 'Hello'

def null_decorator(fun): # функции-обертка
    return fun

def exclaim_decortor(func):
    def wrapper():
        return func() + '!'
    return wrapper

# say_hello=null_decorator(say_hello)
#
# print(say_hello, type(say_hello))
# print(say_hello())

say_hello = exclaim_decortor(say_hello)
print(say_hello, type(say_hello))
print(say_hello())
