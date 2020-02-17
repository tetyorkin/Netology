# Задача №1
# Функция make_cook_book(name_file) генерирует словарь из файла recipes.txt


def make_cook_book(name_file):
    cook_book = {}
    with open(name_file, encoding='utf-8') as file:
        for line in file:
            head = line.strip()
            count = file.readline().strip()
            ingredients = []
            for item in range(0, int(count)):
                ingredient = file.readline().split('|')
                all_ingredients = {'ingredient_name': ingredient[0].strip(),
                                   'quantity': int(ingredient[1]),
                                   'measure': ingredient[2].strip()}
                ingredients.append(all_ingredients)
            file.readline()
            cook_book.update({head: ingredients})
        return cook_book


# Задача №2
# Функция get_shop_list_by_dishes(dishes, person_count) возвращает индегриенты и их количество, согласно шаблону
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cook_book = make_cook_book('recipes.txt')
    for dish in dishes:
        for ingredients in cook_book[dish]:
            buffer_shop_list = dict(ingredients)
            if buffer_shop_list['ingredient_name'] not in shop_list:
                shop_list[buffer_shop_list['ingredient_name']] = \
                    {'measure': buffer_shop_list['measure'],
                     'quantity': buffer_shop_list['quantity'] * person_count}
            else:
                add_quantity = shop_list[buffer_shop_list['ingredient_name']]['quantity']
                shop_list[buffer_shop_list['ingredient_name']] = \
                    {'measure': buffer_shop_list['measure'],
                     'quantity': buffer_shop_list['quantity'] * person_count + add_quantity}
    return shop_list


# Функция врзвращает существующие блюда
def dishes_true():
    cook_book = make_cook_book('recipes.txt')
    dishes = ""
    for dish in cook_book:
        dishes += dish + ", "
    return dishes[:-2]


def wait_input():
    while True:
        user_input = input("Введите номер задачи. 1 или 2: ")
        if user_input == "1":
            print(make_cook_book('recipes.txt'))
        elif user_input == "2":
            try:
                print(f"На данный момент доступны следющие блюда: {dishes_true()}")
                dishes = input("Введите блюда через запятую, на которые необходимо произвести расчёт: ").split(', ')
                person_count = int(input("Введите количество человек на которых необходимо приготовить: "))
                print(get_shop_list_by_dishes(dishes, person_count))
            except KeyError:
                print("Блюдо не найдено")
        else:
            print("Вы ввели что то не то. Попробуйте ещё раз!")


if __name__ == "__main__":
    wait_input()
