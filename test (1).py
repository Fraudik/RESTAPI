from requests import get, post, delete
print(post('http://127.0.0.1:8080/api/v2/jobs',
           json={'id': 1,
                 'team_leader': 'Иванов Степан',
                 'job': 'Стройка',
                 'work_size': 28,
                 'collaborators': '1, 2, 3',
                 'start_date': '2400-11-1',
                 'end_date': '2401-1-1',
                 'is_finished': 1}).json())
# запись

print(post('http://127.0.0.1:8080/api/v2/jobs',
           json={'id': 2,
                 'team_leader': 'Кричиенко Иван',
                 'job': 'Уборка',
                 'work_size': 10,
                 'collaborators': '6, 7',
                 'start_date': '2401-1-1',
                 'end_date': '2401-1-2',
                 'is_finished': 0}).json())
# и еще одна

print(post('http://127.0.0.1:8080/api/v2/jobs',
           json={'id': 2,
                 'team_leader': 'Кричиенко Иван',
                 'job': 'Уборка',
                 'collaborators': '6, 7',
                 'end_date': '2401-1-2',
                 'is_finished': 0}).json())
# неправильная, не все параметры

print(get('http://localhost:8080/api/v2/jobs').json())
# вывод всех записей

print(get('http://localhost:8080/api/v2/jobs/2').json())
# и одной

print(get('http://localhost:8080/api/v2/jobs/999').json())
# неправильная. такого id нет в базе

print(delete('http://localhost:8080/api/v2/jobs/1').json())
# удаление записи

print(get('http://localhost:8080/api/v2/jobs').json())
# вывод всех записей для проверки

print(post('http://127.0.0.1:8080/api/v2/users',
           json={'id': 1,
                 'surname': 'Иванов',
                 'name': 'Степан',
                 'age': 28,
                 'position': 'капитан',
                 'speciality': 'инженер',
                 'address': 'капитанский мостик',
                 'email': 'stealing_ships@figvam.com',
                 'hashed_password': 'qwemty',
                 'modified_date': '2042-12-10'}).json())
# запись

print(post('http://localhost:8080/api/v2/users',
           json={'id': 2,
                 'surname': 'Паролюков',
                 'name': 'Андрей',
                 'age': 35,
                 'position': 'бывшый капитан корабля',
                 'speciality': 'капитан космического корабля',
                 'address': 'за дверью',
                 'email': 'going_return_ship@mess.net',
                 'hashed_password': 'tirexsis',
                 'modified_date': '2042-12-11'}).json())
# и еще одна

print(post('http://localhost:8080/api/v2/users',
           json={'id': 2,
                 'surname': 'Паролюков',
                 'name': 'Андрей',
                 'age': 35,
                 'position': 'бывшый капитан корабля',
                 'speciality': 'капитан космического корабля',
                 'address': 'за дверью',
                 'email': 'going_return_ship@mess.net',
                 'modified_date': '2042-12-11'}).json())
# неправильная, не все параметры

print(get('http://localhost:8080/api/v2/users').json())
# вывод всех записей

print(get('http://localhost:8080/api/v2/users/2').json())
# и одной

print(get('http://localhost:8080/api/v2/users/999').json())
# неправильная. такого id нет в базе

print(delete('http://localhost:8080/api/v2/users/1').json())
# удаление записи

print(get('http://localhost:8080/api/v2/users').json())
# вывод всех записей для проверки
