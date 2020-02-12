def split_on(what, delimiter=""):
    splitted = [[]]
    for item in what:
        if item == delimiter:
            splitted.append([])
        else:
            splitted[-1].append(item)
    return splitted


def open_file(name_file):
    with open(name_file, encoding='utf-8') as file:
        cook_book = {}
        receptes = []
        for line in file:
            recept = line.strip()
            receptes.append(recept)
        receptes_1 = split_on(receptes)
        for item in receptes_1:
            indegrient = item[2:-1]
            print(indegrient)
        #     cook_book.update({item[0]:item[1:]})
        # print(cook_book)


if __name__ == "__main__":
    open_file('recipes.txt')
