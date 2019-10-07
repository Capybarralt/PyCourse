"""
Контекстный менеджер

try:
    f = open(filename)
finally:
    f.close()

"""

with open('out.txt') as f:
    print(f.read())
