import requests
import time
import private  # импортируем token

TOKEN = private.TOKEN
URL = 'https://api.vk.com/method/'
VERSION_API = '5.103'


class User:
    def __init__(self, user_id, first_name=None, last_name=None):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name

    # Метод для определения имени по id
    def get_name(self):
        url = f'https://api.vk.com/method/users.get'
        params = {
            'access_token': TOKEN,
            'user_id': self.user_id,
            'v': '5.103'
        }
        response = requests.get(url, params=params)
        for dict_user in (response.json()['response']):
            name = f"{dict_user['first_name']} {dict_user['last_name']}"
            return name

    # Метод определения id
    def get_user_id(self):
        return self.user_id

    # Метод вывода на экран ссылки
    def __str__(self):
        return self.get_link()

    # Метод переопределения оператора &
    def __and__(self, other):
        user1 = (self.user_id)
        user2 = (other.user_id)
        return self.friends_mutual(user1, user2)

    # Метод определения друзей пользователя
    def get_friends(self):
        method = 'friends.get'
        url = f'{URL}{method}'
        params = {
            'access_token': TOKEN,
            'user_id': self.user_id,
            'v': VERSION_API
        }
        response = requests.get(url, params=params)
        count = response.json()['response']['count']
        user_list = (response.json()['response'])
        user_list_in = user_list['items']
        return f'количество друзей {count} список id друзей {user_list_in}'

    # Метод создания ссылки на профиль
    def get_link(self):
        method = 'users.get'
        url = f'{URL}{method}'
        params = {
            'access_token': TOKEN,
            'user_id': self.user_id,
            'fields': 'screen_name',
            'v': VERSION_API
        }
        response = requests.get(url, params=params)
        dict_user = {}
        if 'error' in response.json().keys():
            print(f"Ошибка!  {response.json()['error']['error_msg']}")
        else:
            for dict_user in (response.json()['response']):
                pass
            link = f"https://vk.com/{dict_user['screen_name']}"
            return link


    # Метод опредления общих друзей между пользователями user1 и user2
    def friends_mutual(self, user1, user2):
        method = 'friends.getMutual'
        url = f'{URL}{method}'
        params = {
            'access_token': TOKEN,
            'source_uid': f'{user1}',
            'target_uid': f'{user2}',
            'v': VERSION_API
        }
        response = requests.get(url, params=params)
        i = 0
        count = len(response.json()['response'])
        if count != 0:
            # return response.json()['response']
            print(f"Всего общих друзей у пользователей {user1} и {user2} - {len(response.json()['response'])}, "
                  f"список их id:\n"
                  f"{response.json()['response']}")
        else:
            return 'Нет друзей'


def main():
    try:
        # Определяем пользователей на основе класса User()
        user1 = User(12249497)
        user2 = User(35007449)
        # Выводим на экран ссылки на профиля пользователей
        print(user1)
        print(user2)
        # Находим id общих друзей user1 и user2
        user1 & user2
        print(f"У пользователя '{user1.get_name()}' страница {user1} его id {user1.get_user_id()}\n"
              f"У пользователя '{user2.get_name()}' страница {user2} его id {user2.get_user_id()}\n")
    except TypeError:
        print('Не удалось вывести содержимое! Сообщение об ошибке выше')


if __name__ == '__main__':
    main()
