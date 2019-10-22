"""
Декораторы

def decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

"""

import pickle
import time

def benchmark(func):
    def wrapper(*args, **kwargs):
        started = time.time()
        result = func(*args, **kwargs)
        worked = time.time() - started
        template = 'Функция "{}" выполнилась за {:f} микросекунд'
        print(template.format(
            func.__name__, worked * 1e6
        ))
        return result
    return wrapper

def cache(func):
    memory = {}

    def wrapper(*args, **kwargs):
        key = pickle.dumps((args, sorted(kwargs.items())))

        if key not in memory:
            memory[key] = func(*args, **kwargs)

        return memory[key]
    return wrapper

@cache
@benchmark  # задекарировали
def factorial(n):
    f = 1

    for i in range(1, n + 1):
        f *= i

    return f

print(f'Факториал числа 10 = {factorial(10)}')
print(f'Факториал числа 15 = {factorial(15)}')
print(f'Факториал числа 10 = {factorial(10)}')
