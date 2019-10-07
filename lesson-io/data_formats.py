"""
Форматы данных

"""

data = {
    'users': [
        {
            'id': 1,
            'name': 'Linus Torvald',
            'skills': ('C++', 'Linux'),
            'is_student': False,
        },
        {
            'id': 2,
            'name': 'Richard Stallman',
            'skills': ('C++', 'C', 'GNU'),
            'is_student': True,
        },
    ],
}

# todo: Pickle
# Для Python
# сериализовать / десериализовать
import pickle

with open('users.pickle', 'wb') as f:
    pickle.dump(data, f)

with open('users.pickle', 'rb') as f:
    loaded_data = pickle.load(f)
    print(f'Прочитано из Pickle: \n{loaded_data}')

# todo: JSON (JavaScript Object Notation)

import json

with open('users.json', 'w') as f:
    json.dump(data, f, indent=4)

with open('users.json', 'r') as f:
    loaded_data = json.load(f)
    print(f'Прочитнано из JSON: \n{loaded_data}')

# кортеж преобразуется в список

"""
todo: CSV

id;name;skills;is_student
1;Linus Torvald;C++;0
2;Richard Stallman;GNU,C;1

"""
import csv

with open('users.csv', 'w') as f:  # можно дописывать
    users = data.get('users', [])

    if users:
        fieldnames = users[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(users)

with open('users.csv') as f:
    reader = csv.DictReader(f)
    users = list(reader)
    print(f'Прочитано из CSV: \n {users}')

"""
todo: INI - модуль configparser

debug 1

db.host localhost
db.user root

[db]
host localhost
user root

И другие варианты

"""

"""
todo: XML - модуль lxml

<users>
    <user>
        <id>1</id>
        <name>Linus Torvald</name>
        ...
    </user>
</users>

"""

"""
todo: Yml/Yaml
Похож на Python
Больше конфиг

"""
