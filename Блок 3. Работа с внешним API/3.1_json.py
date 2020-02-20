import json
from collections import Counter

NAME_FILE = 'newsafr.json'


def read_file(file_name):
    with open(file_name, encoding='utf-8') as f:
        file_content = f.read()
        templates = json.loads(file_content)
        return templates


def more_six(item):
    new = item['rss']['channel']['items']
    big_word = []
    for key in new:
        item = key['description'].split()
        for word in item:
            if len(word) > 6:
                big_word.append(word.lower())
    return big_word


def most_wanted(item):
    big_word_sorted = sorted(item)
    counter = Counter(big_word_sorted)
    most_popular = dict(counter.most_common(10))
    print(f'Топ 10 часто встречающихся слов в новостях из файла {NAME_FILE} следующие:')
    num_str = 1
    for key, count in most_popular.items():
        print(f'Место {num_str}: слово "{key}" встречается - {count} раз')
        num_str += 1


if __name__ == '__main__':
    new_dict = read_file(NAME_FILE)
    big_world = more_six(new_dict)
    most_wanted(big_world)
