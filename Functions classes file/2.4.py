def make_cook_book(name_file):
    cook_book = {}
    with open(name_file, encoding='utf-8') as file:
        for line in file:
            head = line.strip()
            count_ingredients = int(file.readline().strip())
            ingredients = []
            for item in range(count_ingredients):
                ingredient = file.readline().split('|')
                all_ingredients = {'ingredient_name': ingredient[0].strip(),
                                   'quantity': int(ingredient[1]),
                                   'measure': ingredient[2].strip()}
                ingredients.append(all_ingredients)
            file.readline()
            cook_book.update({head: ingredients})
    return cook_book


if __name__ == "__main__":
    print(make_cook_book('recipes.txt'))
