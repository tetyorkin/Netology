import requests as r
import datetime as dt
import cookie

url = cookie.URL_TASK2

header = {
    "Cookie": f'_netology-on-rails_session={cookie.Cookie}',
    'User-Agent': cookie.user_agent_val
}


response = r.get(url, headers=header)
users = []
users_dict = {}
i = 0
c = 0
a = 0
b = 0
d = 0
j = 0
print('Num.|ID     | Имя                     | Заданий | Рейтинг|')
print('-' * 58)
for dict_user in response.json():
    i += 1
    edit_users = {dict_user['name']: dict_user['rating']}
    name = dict_user['name']
    rating = dict_user['rating']
    id_user = dict_user['id']
    buff = ""
    count = rating // 10
    print(f'{i:<4}|{id_user}| {name:24}| {count:^8}| {rating:^7}|')
    if count == 13:
        c += 1
    elif count == 0:
        a += 1
    elif 10 <= count < 13:
        b += 1
    elif 5 < count < 10:
        d += 1
    elif 0 < count < 6:
        j += 1
print(f'\nНа время {dt.datetime.utcnow():%Y.%b.%d %H:%M} по UTC, статистика по группе PY-29 \'Основы языка '
      f'программирования Python\'  следующая:')
print('-' * 51)
print('Описание                      | Студенты | Процент|')
print('-' * 51)
print(f'Закончили курс, сдали диплом  |{c:^10}|{c / i:^8.2%}|')
print(f'Допущено к диплому            |{b:^10}|{b / i:^8.2%}|')
print(f'Выполнено заданий от 1 до 5   |{j:^10}|{j / i:^8.2%}|')
print(f'Выполнено заданий от 6 до 9   |{d:^10}|{d / i:^8.2%}|')
print(f'Не выполнено ни одного задания|{a:^10}|{a / i:^8.2%}|')
print('-' * 51)
print(f'Общее количество              |{c+b+d+a+j:^10}|{(c+b+d+a+j)/i:^8.0%}|')
print('-' * 51)

