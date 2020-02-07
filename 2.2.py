# Введём коэфицент добавления массы животного от количества съеденой им еды - 0,17
WEIGHT_FOOD = 0.17


# Родительский класс для всех животных
class Animals:

    # Метод будет принимать аргументы имени, массы животного и его кормления.
    def __init__(self, name, weight, meal, voice):
        self.__name = name
        self.__meal = meal
        self.__weight = weight
        self.__voice = voice

    # Метод для добавления имени животного
    def set_name(self, name):
        self.__name = name

    # Метод для добавления массы животного
    def set_weight(self, weight):
        self.__weight = weight

    # Метод для добавления значения количества еды и прибаления массы от еды.
    def set_meal(self, meal):
        self.__meal = meal
        self.__weight.append(meal * WEIGHT_FOOD)

    # Метод для добавления голоса животному
    def set_voice(self, voice):
        self.__voice = voice

    # Метод отображения текущей массы
    def get_weight(self):
        return self.__weight

    # Метод отображения съеденой еды
    def get_meal(self):
        return self.__meal

    # Метод воспроизведения голоса животного
    def get_voice(self):
        return self.__voice


class Goose(Animals):
    def __init__(self, name, weight, meal, voice):
        Animals.__init__(self, name, weight, meal, voice)


class Cow(Animals):
    def __init__(self, name, weight, meal, voice):
        Animals.__init__(self, name, weight, meal, voice)


class Sheep(Animals):
    def __init__(self, name, weight, meal, voice):
        Animals.__init__(self, name, weight, meal, voice)


class Chicken(Animals):
    def __init__(self, name, weight, meal, voice):
        Animals.__init__(self, name, weight, meal, voice)


class Goat(Animals):
    def __init__(self, name, weight, meal, voice):
        Animals.__init__(self, name, weight, meal, voice)


class Duck(Animals):
    def __init__(self, name, weight, meal, voice):
        Animals.__init__(self, name, weight, meal, voice)
