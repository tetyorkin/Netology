import requests

FILE_DE = 'DE.txt'
FILE_ES = 'ES.txt'
FILE_FR = 'FR.txt'
API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
URL1 = 'https://translate.yandex.net/api/v1.5/tr.json/getLangs'


def open_read_file(file):
    with open(file, encoding='utf-8') as file:
        read = file.readlines()
        buf = ','.join(read)
        text = buf.replace('\n,', '\n')
    return text


def lang(file):
    language = file[0:2].lower()
    return language


# def support_lang(file):
#     lang_first = lang(file)
#     params = {
#         'key': API_KEY
#     }
#     response = requests.get(URL1, params=params)
#     support_translate = response.json()['dirs']
#     support_text = ', '.join(support_translate)
#     text = support_text
#     print(f"По названию файла определён язык '{lang_first}', "
#           f"Yandex поддерживет перевод с этого языка на следующие языки:")
#     for line in support_translate:
#             if line[:2] == lang_first:
#                 print(line[-2:])

# def support_lang_test(file1, file2, file3):
#     lang_first1 = lang(file1)
#     lang_first2 = lang(file2)
#     lang_first3 = lang(file3)
#     params = {
#         'key': API_KEY
#     }
#     response = requests.get(URL1, params=params)
#     support_translate = response.json()['dirs']
#     support_lang_from_file = set()
#     print(f"По названиям файлов определёны следующие коды языков '{lang_first1}', '{lang_first2}' и '{lang_first3}'"
#           f" У данных языков, согласно Yandex.Переводчик есть следующие общие направления переводов:")
#     for line in support_translate:
#             if line[:2] == lang_first1:
#                 support_lang_from_file.add((line[-2:]))
#             elif line[:2] == lang_first2:
#                 support_lang_from_file.add((line[-2:]))
#             elif line [:2] == lang_first3:
#                 support_lang_from_file.add((line[-2:]))
#     print(support_lang_from_file)

def translate_it(file, to_lang):
    text = open_read_file(file)
    language = lang(file)
    params = {
        'key': API_KEY,
        'text': text,
        'lang': f"{language}-{to_lang}"
    }
    response = requests.get(URL, params=params)
    translated_list = response.json()['text']
    translated_text = ','.join(translated_list)
    print(translated_text)

# def write_to_file()


if __name__ == '__main__':
    to_lang = input("На какой язык произвести перевод? (по умолчанию русский) ")
    if to_lang == '':
        to_lang = 'ru'
    translate_it(FILE_DE, to_lang)
    translate_it(FILE_ES, to_lang)
    translate_it(FILE_FR, to_lang)


