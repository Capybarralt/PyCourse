"""
Декораторы с параметрами

def parametrize(<параметры декоратора>):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator

"""

import textwrap
from datetime import datetime

def log(filename):
    template = textwrap.dedent('''
    [{now: %Y-%m-%d %H:%M:%S}] Function "{func}" called with:
        -> positional arguments: {args}
        -> keyword arguments:    {kwargs}
    Return: {result}
    ''')
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, 'a') as f:
                f.write(template.format(
                    now=datetime.now(),
                    func=f'{func.__module__}.{func.__name__}',
                    args=args,
                    kwargs=kwargs,
                    result=result
                ))
        return wrapper
    return decorator

@log('log.txt')
def f(a,b):
    return a + b

f(1, 2)
f(3, 4)
