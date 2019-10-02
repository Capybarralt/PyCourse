"""
todo: Ветвление
"""

# a = int(input())
# b = int(input())
#
# if a > b:
#     print('a > b')
#
#     if a is None:
#         pass
# elif a == b:
#     print('a = b')
# else:
#     print('a < b')


"""
todo: Циклы

break    - мгновенно прервать работу цикла
continue - пропустить текущую итерацию !!!!
"""

i = 1

while i <= 10:
    i += 1

print(i)


j = 1

while True:
    if j >= 5:
        break
    j += 1



for i in range(5):
    print(i)


d = {
    'firstname': 'Вася',
    'lastname': 'Пупкин',
    'age': 1000,
}

for key, value in d.items():
    print(key, value)


person = ('Вася', 'Пупкин', 1000)

for i, v in enumerate(person):
    print(i, v)



"""
todo: Как не нужно генерировать строки!!!!
"""

s = ''

for i in range(5):
    s += str(i)

print(s)


"""
todo: Как нужно генерировать строки!!!!
"""

s = []

for i in range(5):
    s.append(str(i))

s = ''.join(s) # все элементы должны быть строками

print(s)
