def greetin_username(name):
    return f'Hello, {name}'

def good_bye(firstname, lastname):
    return f'Good bye, {firstname} {lastname}'

def exclaim_decortor(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + '!'
    return wrapper

greetin_username = exclaim_decortor(greetin_username)
good_bye = exclaim_decortor(good_bye)

print(greetin_username('Вася'))
print(good_bye('Вася', 'Пупкин'))
