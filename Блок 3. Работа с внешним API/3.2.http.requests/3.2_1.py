import requests
import os

FILE_DE = 'DE.txt'
FILE_ES = 'ES.txt'
FILE_FR = 'FR.txt'
FILE_SUPPORT = 'support_lang.txt'
API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
URL1 = 'https://translate.yandex.net/api/v1.5/tr.json/getLangs'


# Изначально написал функцию проверяющую поддержку языка перевода. Но API Яндекса возвращает только 33
# поддерживаемых языка. Хотя на самом деле их 93. Добавил файл со списком поддерживаемых языков
#  Функция support_lang() считывает файл со списком поддерживаемых языков и возвращает словарь
def support_lang(file):
    with open(file, encoding='utf-8') as file:
        support = {}
        for line in file:
            dict_lang = {line.split()[0]: line.split()[1]}
            support.update(dict_lang)
    return support


# Отрываем и читаем файл, вовращвем его как строку
def open_read_file(file):
    with open(file, encoding='utf-8') as file:
        read = file.readlines()
        buf = ','.join(read)
        text = buf.replace('\n,', '\n')
    return text


# Определяем язык файла по названию файла
def lang(file):
    language = file[0:2].lower()
    return language


# Перводим текст, в нужном направлении и возвращвем перевод
def translate_it(file, to_lang):
    text = open_read_file(file)
    from_lang = lang(file)
    params = {
        'key': API_KEY,
        'text': text,
        'lang': f"{from_lang}-{to_lang}"
    }
    response = requests.get(URL, params=params)
    translated_list = response.json()['text']
    translated_text = ','.join(translated_list)
    return translated_text


# Выбор языка на который хотим перевести
def choose_lang(to_lang):
    if to_lang == '':
        to_lang = 'ru'
    return to_lang


# Если нет файла создаём, если есть, записываем результат перевода в конец файла.
# Перевод всех файлов пишется в один новый файл
def write_to_file(file):
    with open(new_file_name, 'a', encoding='utf-8') as f:
        to_language = str(choose_lang(input_lang))
        translate_text = translate_it(file, to_language)
        f.writelines(f'-----------------------------------\n'
                     f'translate from {lang(file).upper()} to {to_language.upper()}\n'
                     f'{translate_text}\n')


# input_lang - пользователь выбирает язык на который необходимо перевести текст.
# На основе выбора языка выбирается имя нового файла, если файл с таким именем уже существует, он удаляется.
if __name__ == '__main__':
    support_lang = support_lang(FILE_SUPPORT)
    input_lang = input(f"На какой язык произвести перевод? (Без указания, будет выбран русский язык)\n"
                       f"Для перевода доступны следующие языки: {support_lang}\n")
    if input_lang in support_lang.values() or input_lang == '':
        new_file_name = f"translate_to_{choose_lang(input_lang).upper()}.txt"
        if os.path.exists(new_file_name):
            os.remove(new_file_name)
        choose_lang(input_lang)
        write_to_file(FILE_DE)
        write_to_file(FILE_ES)
        write_to_file(FILE_FR)
        print('Файл с переводом готов')
    else:
        print(f"К сожалению  выбранный язык не поддерживается")
