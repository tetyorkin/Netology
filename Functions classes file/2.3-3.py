documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "100089", "name": "Иванов Генрих"},
    {"type": "insurance", "number": "315151"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
}


# Поиск номера документа вынес в отдельную функцию
def number_id(num_doc):
    count = 0
    for name in documents:
        if num_doc == name['number']:
            count = count - len(documents)
        else:
            count = count + 1
    if count == -1:
        return 1  # Необходим при вызове функции перемещения doc_move()
    else:
        print("Документ с данным номером не найден в сиске документов")


# Проверка на пустую строку и наличие допустимой команды
# Исправил условия. Команды добавил в список
def zero(item):
    string = "допустимые команды: p, l, s, a, d, m, as, n"
    input_user = ['a', 'p', 'l', 's', 'd', 'm', 'as', 'n']
    if item in input_user:
        return item
    if item == '':
        print(f"Ничего не введено, {string}")
    else:
        print(f"Команды не найдено, {string}")


# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
def name_document():
    num_doc = input("Введите номер документа: ")
    number_id(num_doc)
    for name in documents:
        if num_doc == name['number']:
            print(f"На документе с номером '{name['number']}' имя - {name['name']}")


# l  list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
def all_document():
    for all_doc in documents:
        print(f"{all_doc['type']} \"{all_doc['number']}\" \"{all_doc['name']}\"")


# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
def shelf():
    num_doc = input("Введите номер документа: ")
    number_id(num_doc)
    for shelf_id, number in directories.items():
        if num_doc in number:
            print(f"Документ с номером '{num_doc}' найден на полке - {shelf_id}")


# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца
# и номер полки, на котором он будет храниться.
def add_document():
    documents_add = {}
    document_type = input("Введите тип документа: ")
    document_id = input("Введите номер документа: ")
    document_name = input("Введите имя владельца: ")
    document_shelf = input("Введите номер полки: ")
    if int(document_shelf) in range(0, len(directories) + 1):
        documents.append(documents_add)
        directories[document_shelf].append(document_id)
        documents_add.update({'type': document_type, 'number': document_id, 'name': document_name})
        print(f'В список документов была добавлена слелующая запись в виде словаря "{documents_add}" '
              f'и добавлена на полку "{document_shelf}"')
    else:
        print("Указаной полки не существует")


# d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
def del_document():
    document_id = input("Введите номер документа: ")
    number_id(document_id)
    for document_find in documents:
        if document_id == document_find['number']:
            documents.remove(document_find)
            print(f"Документ с номером {document_id} удалён из списка документов")
            print(documents)
    for shelf_id, numbers in directories.items():
        if document_id in numbers:
            numbers.remove(document_id)
            print(f"Документ с номером {document_id} удалён из перечня полок")
            print(directories)


# m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
def doc_move():
    document_id = input("Введите номер документа: ")
    aim_shelf = input("Введите номер полки куда переместить документ: ")
    if number_id(document_id) == 1:
        if int(aim_shelf) in range(0, len(directories) + 1):
            for shelf_id, numbers in directories.items():
                if document_id in numbers:
                    numbers.remove(document_id)
                    directories[aim_shelf].append(document_id)
            print(f"Документ с номером '{document_id}' перемещён на полку под номером {aim_shelf}")
            print(directories)
        else:
            print("Такой полки не существует")


# as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень;
def add_shelf():
    new_shelf = input("Введите номер новой полки: ")
    directories.setdefault(new_shelf, [])
    print(f"Создана полка номер {new_shelf}")
    print(directories)


# Добавлена функция отображения имени у документа
def show_name():
    try:
        for name in documents:
            print(name['name'])
    except KeyError:
        print("Ошибка. У одного из документов нет имени")


def main():
    while True:
        user_input = input("Введите команду: ")
        zero(user_input)
        if user_input == 'p':
            name_document()
        elif user_input == 'l':
            all_document()
        elif user_input == 's':
            shelf()
        elif user_input == 'a':
            add_document()
        elif user_input == 'd':
            del_document()
        elif user_input == 'm':
            doc_move()
        elif user_input == 'as':
            add_shelf()
        elif user_input == 'n':
            return show_name()


main()
