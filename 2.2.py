# Введём коэфицент добавления массы животного от количества съеденой им еды - WEIGHT_FOOD
# Коэфицент снятия профита с птиц - PROFIT_EGGS
# Коэфицент снятия профита с парнокопытных - PROFIT_MILK
# Коэфицент снятия профита с овец - PROFIT_WOOL
WEIGHT_FOOD = 0.2
PROFIT_EGGS = 0.05
PROFIT_MILK = 0.4
PROFIT_WOOL = 0.02


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
        self.set_weight(self.get_weight() + (meal * WEIGHT_FOOD))

    def set_voice(self, voice):
        self.__voice = voice

    def get_name(self):
        return self.__name

    # Метод отображения текущей массы
    def get_weight(self):
        return self.__weight

    # Метод отображения съеденой еды
    def get_meal(self):
        return self.__meal

    # Метод воспроизведения голоса животного
    def get_voice(self):
        return self.__voice


class Birds(Animals):
    def __init__(self, name, weight, meal, voice, eggs):
        Animals.__init__(self, name, weight, meal, voice)
        self.__eggs = eggs

    def set_eggs(self, eggs):
        self.__eggs = eggs
        self.set_weight(self.get_weight() - (eggs * PROFIT_EGGS))

    def get_eggs(self):
        if self.get_weight() > 0:
            return self.__eggs


class MilkAnimals(Animals):
    def __init__(self, name, weight, meal, voice, milk):
        Animals.__init__(self, name, weight, meal, voice)
        self.__milk = milk

    def set_milk(self, milk):
        self.__milk = milk
        self.set_weight(self.get_weight() - (milk * PROFIT_MILK))

    def get_milk(self):
        if self.get_weight() > 0:
            return self.__milk


class Goose(Birds):
    def __init__(self, name, weight, meal, voice, eggs):
        Birds.__init__(self, name, weight, meal, voice, eggs)


class Cow(MilkAnimals):
    def __init__(self, name, weight, meal, voice, milk):
        MilkAnimals.__init__(self, name, weight, meal, voice, milk)


class Sheep(Animals):
    def __init__(self, name, weight, meal, voice):
        Animals.__init__(self, name, weight, meal, voice)


class Chicken(Birds):
    def __init__(self, name, weight, meal, voice, profit, eggs):
        Birds.__init__(self, name, weight, meal, voice, eggs)


class Goat(Animals):
    def __init__(self, name, weight, meal, voice):
        Animals.__init__(self, name, weight, meal, voice)


class Duck(Birds):
    def __init__(self, name, weight, meal, voice, profit, eggs):
        Birds.__init__(self, name, weight, meal, voice, eggs)


def gooses():
    goose1 = Goose("", 0, 0, "", 0)
    goose2 = Goose("", 0, 0, "", 0)
    goose1.set_name("Серый")
    goose2.set_name("Белый")
    goose1.set_weight(6000)
    goose2.set_weight(6500)

    print("\n{:*^90}".format("Гуси"))
    print(f"У бабуси живёт два гуся один {goose2.get_name()}, другой {goose1.get_name()}\n"
          f"{goose2.get_name()} масса = {goose2.get_weight()}\n"
          f"{goose1.get_name()} масса = {goose1.get_weight()}")
    goose2.set_meal(500)
    goose1.set_meal(700)
    print(f"Покормила их бабушка: {goose2.get_name()} съел {goose2.get_meal()}  грамм пшена "
          f"{goose1.get_name()} съел {goose1.get_meal()}  грамм пшена\n"
          f"После усвоения еды масса у гусей изменилась:\n"
          f"{goose2.get_name()} масса = {goose2.get_weight()}\n"
          f"{goose1.get_name()} масса = {goose1.get_weight()}")
    goose1.set_eggs(2)
    goose2.set_eggs(2)
    print(f"После отдыха гусей бабушка собрала у гусей яйца по {goose1.get_eggs()} у каждого и их маасса изменилась\n"
          f"{goose2.get_name()} масса = {goose2.get_weight()}\n"
          f"{goose1.get_name()} масса = {goose1.get_weight()}")
    goose1.set_voice("Га Га Га")
    goose2.set_voice("Га Га Га")
    print(f"И стали гуси от такой беззаботной жизни гагатать и {goose1.get_name()}, и {goose2.get_name()} "
          f"-'{goose1.get_voice()}'"
          f" -'{goose2.get_voice()}'")


gooses()


def cow():
    cow1 = Cow("Манька", 100000, 0, "", 0)
    weight_kg = cow1.get_weight() / 1000
    print("\n{:*^90}".format("Корова"))
    print(f"У бабушки есть корова, корову звать - {cow1.get_name()}, "
          f"масса коровы {weight_kg} кг.")
    cow1.set_meal(15000)
    print(f"Съела {cow1.get_name()}  {cow1.get_meal() / 1000} кг. травы "
          f"и её масса после усвоения еды изменилась до {cow1.get_weight() / 1000} кг.")
    cow1.set_milk(20000)
    cow1.set_voice("Муууу, Мууууу")
    print(f"Подоила бабушка корову и выдоила у неё {cow1.get_milk() / 1000} литров молока "
          f"и похудела {cow1.get_name()} до {cow1.get_weight() / 1000} кг\n"
          f"И замычала {cow1.get_name()} от тоски "
          f"-'{cow1.get_voice()}'")


cow()
