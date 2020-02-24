import os
import re
import requests
from task_1 import *  # импортируем задачу №1, чтобы воспользоваться функцией 'open_read_file(file)'
from private import *  # импортируем файл private.py для доступа к токену в котором он лежит

URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload?'
TOKEN = TOKEN


# С помощию регулярных выражений ищем в текущей директории все файлы, которые были переведены и возвращаем их список
def find_translate_file():
    files = os.listdir(path=".")
    files_list = re.findall(r'translate_to_.+?xt', str(files))
    return files_list


# Функция отправки файлов на диск. Циклом проходимся по всем файлам, которые найдены.
# Действия функции разделены на два этапа
# 1 Сначала запрашивается ссылка для загрузки
# 2 методом PUT отправляем файл по полученой ссылке из 1-го этапа
def upload_files():
    # 1 этап
    headers = {'Authorization': TOKEN,
               'Accept': 'application/json'}
    for name in find_translate_file():
        params = {
            'path': f'/Нетология/{name}',
            'overwrite': 'true'
        }
        response = requests.get(URL, headers=headers, params=params)
        # 2 этап
        link = response.json()['href']
        files = {
            'file': open_read_file(name).encode('utf-8')
        }
        requests.put(url=link, headers=headers, files=files)
        print(f'Файл {name} загружен на яндекс диск')


if __name__ == '__main__':
    upload_files()
    print('------------------------\n'
          'Все файлы загружены')
