import requests
import time
import private  # импортируем token

TOKEN = private.TOKEN


class User:
    def __init__(self, user_id, first_name=None, last_name=None):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        # self.friends_mutual = friends_mutual

    def get_name(self, user_id):
        url = f'https://api.vk.com/method/users.get'
        params = {
            'access_token': TOKEN,
            'user_id': user_id,
            'v': '5.103'
        }
        response = requests.get(url, params=params)
        for dict_user in (response.json()['response']):
            name = f"{dict_user['first_name']} {dict_user['last_name']}"
            return name

    def get_link(self, user_id):
        url = f'https://vk.com/id{user_id}'
        return url

    # def friends_mutual(self, user1, user2):
    #     url = 'https://api.vk.com/method/friends.getMutual'
    #     params = {
    #         'access_token': TOKEN,
    #         'source_uid': user1,
    #         'target_uid': user2,
    #         'v': '5.103'
    #     }
    #     response = requests.get(url, params=params)
    #     i = 0
    #     count = len(response.json()['response'])
    #     if count != 0:
    #         return response.json()['response']
    #     else:
    #         return 'Нет друзей'

    def friends_mutual(self, two_users):
        users = str(two_users)
        user1 = users.split('&')[0].strip(' ')
        user2 = users.split('&')[1].strip(' ')
        url = 'https://api.vk.com/method/friends.getMutual'
        params = {
            'access_token': TOKEN,
            'source_uid': user1,
            'target_uid': user2,
            'v': '5.103'
        }
        response = requests.get(url, params=params)
        print(response.json())
        i = 0
        count = len(response.json()['response'])
        if count != 0:
            return response.json()['response']
        else:
            return 'Нет друзей'

    # def get_friends_mutual(self, user_id):
    #     self.response = user_id


#
#
# def get_info(user_id):
#     params = {
#         'access_token': TOKEN,
#         'user_id': user_id,
#         'v': '5.103'
#     }
#     response = requests.get(URL, params=params)
#     user_list = (response.json()['response'])
#     # print(user_list)
#     dict_user = {}
#     for dict_user in user_list:
#         pass
#     name = f"'{dict_user['first_name']} {dict_user['last_name']}' " \
#            f"ссылка на страницу: https://vk.com/id{dict_user['id']}"
#     return name
#
#
# def get_friends(user_id):
#     params = {
#         'access_token': TOKEN,
#         'user_id': user_id,
#         'v': '5.103'
#     }
#     response = requests.get(URL2, params=params)
#     user_list = (response.json()['response'])
#     count = user_list['count']
#     users_list = user_list['items']
#     count = 0
#     for line in users_list:
#         try:
#             count += 1
#             print(f'{count} {get_info(line)}')
#             time.sleep(0.09)
#         except KeyError:
#             print("Ошибка")
#             continue
#
#
# def get_friends_mutual(user1, user2):
#     params = {
#         'access_token': TOKEN,
#         'source_uid': user1,
#         'target_uid': user2,
#         'v': '5.103'
#     }
#     response = requests.get(URL3, params=params)
#     i = 0
#     count = len(response.json()['response'])
#     if count != 0:
#         print(f'\nУ пользователей {get_info(user1)} и {get_info(user2)} общих друзей - {count}, это следующие друзья:')
#         for line in response.json()['response']:
#             try:
#                 i += 1
#                 print(f'{i} {get_info(line)}')
#                 time.sleep(0.1)
#             except KeyError:
#                 print("Ошибка")
#                 continue
#     else:
#         print(f'\nУ пользователей {get_info(user1)} и {get_info(user2)} нет общих друзей')
def name_user(user_id):
    user = User(user_id)
    return user.get_name(user_id)


def get_friend(users):
    two_users = User(users)
    return two_users.friends_mutual(users)



if __name__ == '__main__':
    # user_input = input("Введите пользователей: ")
    user_input = '35007449 & 12249497'
    print(get_friend(user_input))
    # print(get_friend(12249497, 35007449))
    # print(name_user(12249497))
    # user1 = User(12249497)
    # print(user1.get_name(12249497))

    # get_friends(35007449)
    # print(get_info(35007449))
