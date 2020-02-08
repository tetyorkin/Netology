# Введём коэфицент добавления массы животного от количества съеденой им еды - WEIGHT_FOOD
# Коэфицент уменьшения массы при снятии профита с птиц - PROFIT_EGGS
# Коэфицент уменьшения массы при снятии профита с парнокопытных - PROFIT_MILK
# Коэфицент уменьшения массы при снятии профита с овец - PROFIT_WOOL
WEIGHT_FOOD = 0.2
PROFIT_EGGS = 0.05
PROFIT_MILK = 0.4
PROFIT_WOOL = 0.02


# Родительский класс для всех животных
class Animals:

    # Метод будет принимать аргументы имени, массы животного и его кормления.
    def __init__(self, name, weight, meal, voice):
        self.name = name
        self.meal = meal
        self.weight = weight
        self.voice = voice

    # Метод для добавления имени животного
    def set_name(self, name):
        self.name = name

    # Метод для добавления массы животного
    def set_weight(self, weight):
        self.weight = weight

    # Метод для добавления значения количества еды и прибаления массы от еды.
    def set_meal(self, meal):
        self.meal = meal
        self.set_weight(self.get_weight() + (meal * WEIGHT_FOOD))

    def set_voice(self, voice):
        self.voice = voice

    def get_name(self):
        return self.name

    # Метод отображения текущей массы
    def get_weight(self):
        return self.weight

    # Метод отображения съеденой еды
    def get_meal(self):
        return self.meal

    # Метод воспроизведения голоса животного
    def get_voice(self):
        return self.voice


# Родительский класс для птиц
class Birds(Animals):
    def __init__(self, name, weight, meal, voice, eggs):
        Animals.__init__(self, name, weight, meal, voice)
        self.eggs = eggs

    def set_eggs(self, eggs):
        self.eggs = eggs
        self.set_weight(self.get_weight() - (eggs * PROFIT_EGGS))

    def get_eggs(self):
        if self.get_weight() > 0:
            return self.eggs


# Родительский класс для животных которых можно доить
class MilkAnimals(Animals):
    def __init__(self, name, weight, meal, voice, milk):
        Animals.__init__(self, name, weight, meal, voice)
        self.milk = milk

    def set_milk(self, milk):
        self.milk = milk
        self.set_weight(self.get_weight() - (milk * PROFIT_MILK))

    def get_milk(self):
        if self.get_weight() > 0:
            return self.milk


class Goose(Birds):
    def __init__(self, name, weight, meal, voice, eggs):
        Birds.__init__(self, name, weight, meal, voice, eggs)


class Cow(MilkAnimals):
    def __init__(self, name, weight, meal, voice, milk):
        MilkAnimals.__init__(self, name, weight, meal, voice, milk)


class Sheep(Animals):
    def __init__(self, name, weight, meal, voice, wool):
        Animals.__init__(self, name, weight, meal, voice)
        self.wool = wool

    def set_wool(self, wool):
        self.wool = wool
        self.set_weight(self.get_weight() - (wool * PROFIT_WOOL))

    def get_wool(self):
        if self.get_weight() > 0:
            return self.wool


class Chicken(Birds):
    def __init__(self, name, weight, meal, voice, profit, eggs):
        Birds.__init__(self, name, weight, meal, voice, eggs)


class Goat(MilkAnimals):
    def __init__(self, name, weight, meal, voice, milk):
        MilkAnimals.__init__(self, name, weight, meal, voice, milk)


class Duck(Birds):
    def __init__(self, name, weight, meal, voice, eggs):
        Birds.__init__(self, name, weight, meal, voice, eggs)


def gooses():
    goose1 = Goose("", 0, 0, "Га га Га", 0)
    goose2 = Goose("", 0, 0, "Га га Га", 0)
    goose1.set_name("Серый")
    goose2.set_name("Белый")
    goose1.set_weight(6000)
    goose2.set_weight(6500)
    name_animal = "Гуси"
    print("\n{:*^90}".format(name_animal))
    print(f"Животные - {name_animal}:")
    print(f"{goose1.get_name()} и {goose2.get_name()}")
    print(f"Масса {goose1.get_name()} - {goose1.get_weight() / 1000}\n"
          f"Масса {goose2.get_name()} - {goose2.get_weight() / 1000}")
    goose1.set_meal(2000)
    goose2.set_meal(6000)
    print(f"Приём пищи (масса пищи):\n"
          f"{goose1.get_name()} {goose1.get_meal() / 1000} килограмм\n"
          f"{goose2.get_name()} {goose2.get_meal() / 1000} килограмм")
    print(f"Вес после приёма пищи:\n"
          f"{goose1.get_name()} {goose1.get_weight() / 1000} килограмм\n"
          f"{goose2.get_name()} {goose2.get_weight() / 1000} килограмм")
    goose1.set_eggs(2)
    goose2.set_eggs(6)
    print(f"Вес после забора профита:\n"
          f"{goose1.get_name()} {goose1.get_weight() / 1000:.1f} килограмм\n"
          f"{goose2.get_name()} {goose2.get_weight() / 1000:.1f} килограмм")
    print(f"Подали голос:\n"
          f"{goose1.get_name()} - {goose1.get_voice()}\n"
          f"{goose2.get_name()} - {goose2.get_voice()}")
    weight_goose1 = goose1.get_weight() / 1000
    weight_goose2 = goose2.get_weight() / 1000
    goose_dict = {goose1.get_name(): weight_goose1, goose2.get_name(): weight_goose2}
    return goose_dict


# print(gooses())


def cow():
    cow1 = Cow("Манька", 100000, 0, "Мууу Муму Муууу", 0)
    weight_kg = cow1.get_weight() / 1000
    name_animal = "Корова"
    print("\n{:*^90}".format(name_animal))
    print(f"Животные - {name_animal}:")
    print(f"{cow1.get_name()}")
    print(f"Масса {cow1.get_name()} - {cow1.get_weight() / 1000}")
    cow1.set_meal(15000)
    print(f"Приём пищи:\n"
          f"{cow1.get_name()} {cow1.get_meal() / 1000} килограмм")
    print(f"Вес после приёма пищи:\n"
          f"{cow1.get_name()} {cow1.get_weight() / 1000} килограмм")
    cow1.set_milk(20000)
    print(f"Вес после забора профита:\n"
          f"{cow1.get_name()} {cow1.get_weight() / 1000:.2f} килограмм")
    print(f"Подали голос:\n"
          f"{cow1.get_name()} - {cow1.get_voice()}")
    weight_cow = cow1.get_weight() / 1000
    cows_dict = {cow1.get_name(): weight_cow}
    return cows_dict


# cow()


def goat():
    name_animal = "Овцы"
    goat1 = Goat("Рога", 30000, 0, "Беее Беее", 0)
    goat2 = Goat("Копыта", 25000, 0, "Беее Мееее", 0)
    print("\n{:*^90}".format(name_animal))
    print(f"Животные - {name_animal}:")
    print(f"{goat1.get_name()} и {goat2.get_name()}")
    print(f"Масса {goat1.get_name()} - {goat1.get_weight() / 1000}\n"
          f"Масса {goat2.get_name()} - {goat2.get_weight() / 1000}")
    goat1.set_meal(4000)
    goat2.set_meal(6000)
    print(f"Приём пищи:\n"
          f"{goat1.get_name()} {goat1.get_meal() / 1000} килограмм\n"
          f"{goat2.get_name()} {goat2.get_meal() / 1000} килограмм")
    print(f"Вес после приёма пищи:\n"
          f"{goat1.get_name()} {goat1.get_weight() / 1000} килограмм\n"
          f"{goat2.get_name()} {goat2.get_weight() / 1000} килограмм")
    goat1.set_milk(5000)
    goat1.set_milk(5000)
    print(f"Вес после забора профита:\n"
          f"{goat1.get_name()} {goat1.get_weight() / 1000} килограмм\n"
          f"{goat2.get_name()} {goat2.get_weight() / 1000} килограмм")
    print(f"Подали голос:"
          f"{goat1.get_name()} - {goat1.get_voice()}\n"
          f"{goat2.get_name()} - {goat2.get_voice()}")
    weight_goat1 = goat1.get_weight() / 1000
    weight_goat2 = goat2.get_weight() / 1000
    goats_dict = {goat1.get_name(): weight_goat1, goat2.get_name(): weight_goat2}
    return goats_dict


# goat()


def sheep():
    name_animal = "Овцы"
    sheep1 = Sheep("Барашек", 20000, 0, "Геее гееее", 0)
    sheep2 = Sheep("Кудрявый", 35000, 0, "Гррр грррр", 0)
    print("\n{:*^90}".format(name_animal))
    print(f"Животные - {name_animal}:")
    print(f"{sheep1.get_name()} и {sheep2.get_name()}")
    print(f"Масса {sheep1.get_name()} - {sheep1.get_weight() / 1000}\n"
          f"Масса {sheep2.get_name()} - {sheep2.get_weight() / 1000}")
    sheep1.set_meal(2000)
    sheep2.set_meal(6000)
    print(f"Приём пищи:\n"
          f"{sheep1.get_name()} {sheep1.get_meal() / 1000} килограмм\n"
          f"{sheep2.get_name()} {sheep2.get_meal() / 1000} килограмм")
    print(f"Вес после приёма пищи:\n"
          f"{sheep1.get_name()} {sheep1.get_weight() / 1000} килограмм\n"
          f"{sheep2.get_name()} {sheep2.get_weight() / 1000} килограмм")
    sheep1.set_wool(2000)
    sheep1.set_wool(1500)
    print(f"Вес после забора профита:\n"
          f"{sheep1.get_name()} {sheep1.get_weight() / 1000} килограмм\n"
          f"{sheep2.get_name()} {sheep2.get_weight() / 1000} килограмм")
    print(f"Подали голос:\n"
          f"{sheep1.get_name()} - {sheep1.get_voice()}\n"
          f"{sheep2.get_name()} - {sheep2.get_voice()}")
    weight_sheep1 = sheep1.get_weight() / 1000
    weight_sheep2 = sheep2.get_weight() / 1000
    sheep_dict = {sheep1.get_name(): weight_sheep1, sheep2.get_name(): weight_sheep2}
    return sheep_dict


def duck():
    name_animal = "Утка"
    duck1 = Duck("Кряква", 5000, 0, "Кря Кря Кря", 0)
    print("\n{:*^90}".format(name_animal))
    print(f"Животные - {name_animal}:")
    print(f"{duck1.get_name()}")
    print(f"Масса {duck1.get_name()} - {duck1.get_weight() / 1000}")
    duck1.set_meal(2000)
    print(f"Приём пищи:\n"
          f"{duck1.get_name()} {duck1.get_meal() / 1000} килограмм")
    print(f"Вес после приёма пищи:\n"
          f"{duck1.get_name()} {duck1.get_weight() / 1000} килограмм")
    duck1.set_eggs(3)
    print(f"Вес после забора профита:\n"
          f"{duck1.get_name()} {duck1.get_weight() / 1000:.2f} килограмм")
    print(f"Подали голос:\n"
          f"{duck1.get_name()} - {duck1.get_voice()}")
    weight_duck = duck1.get_weight() / 1000
    ducks_dict = {duck1.get_name(): weight_duck}
    return ducks_dict


def max_weight():
    weight_max = 0
    weight = 0
    weight_all = 0
    all_dict = {}
    all_dict.update(gooses())
    all_dict.update(cow())
    all_dict.update(goat())
    all_dict.update(sheep())
    all_dict.update(duck())
    for key, weight in all_dict.items():
        if weight > weight_max:
            name_animal = key
            weight_max = weight
        weight_all += weight_max
    print(
        f"\nОбщая масса всех животных равна {weight_all:.1f} килограмм, максимальная масса тела у животтного с именем "
        f"{name_animal} и массой {weight_max} килограмм")


if __name__ == "__main__":
    max_weight()
