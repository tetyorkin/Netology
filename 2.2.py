class Animals:

    # Метод будет принимать аргументы имени, массы животного и его кормления.
    def __init__(self, name, weight, meal):
        self.__name = name
        self.__meal = meal
        self.__weight = weight

    # Метод для добавления имени животного
    def set_name(self, name):
        self.__name = name

    # Метод для добавления массы животного
    def set_weight(self, weight):
        self.__weight = weight

    # Метод для добавления значения количества еды
    def set_meal(self, meal):
        self.__meal = meal

    # Метод отображения текущей массы
    def get_weight(self):
        return self.__weight

    # Метод отображения съеденой еды
    def get_meal(self):
        return self.__meal


class Goose(Animals):
    def __init__(self, name, weight, meal, ):
        Animals.__init__(self, name, weight, meal)
