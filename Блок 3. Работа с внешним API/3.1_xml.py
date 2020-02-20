import xml.etree.ElementTree as ET
from collections import Counter

NAME_FILE = 'newsafr.xml'


# Считываем файл возвращаем корень дерева класса 'xml.etree.ElementTree' с которым будем работать
def read_file(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()
    return root


# Продвигаеемся до тега 'description' далее работаем с его атрибутом, ищем слова больше 6 символов
def more_six(core_dict):
    big_word = []
    for child in core_dict:
        for line in child:
            if line.tag == 'item':
                for des in line:
                    if des.tag == 'description':
                        item = des.text.split()
                        for word in item:
                            if len(word) > 6:
                                big_word.append(word.lower())
    return big_word


# Функция more_six_up() поиск слов будет с учётом регистра
def more_six_up(core_dict):
    big_word = []
    for child in core_dict:
        for line in child:
            if line.tag == 'item':
                for des in line:
                    if des.tag == 'description':
                        item = des.text.split()
                        for word in item:
                            if len(word) > 6:
                                big_word.append(word)
    return big_word


# С помощью библиоотеки collections, считаем количество вхождений каждого слова и выводим ТОП 10 слов
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
    while True:
        user_input = input("\nУчитывать регистр при поиске ТОП 10 слов? (да/нет): ")
        new_dict = read_file(NAME_FILE)
        if user_input == 'нет':
            big_world = more_six(new_dict)
            most_wanted(big_world)
        elif user_input == 'да':
            big_world = more_six_up(new_dict)
            most_wanted(big_world)
        else:
            print("Вы ввели что то не то. Попробуйте ещё раз")
