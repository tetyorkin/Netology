#  Реализовать Польскую нотацию для двух положительных чисел.
def polish(item):
    string_input = item
    token = string_input.split(" ")  # разделяем строку по пробелу, для обращения по индексу к числам и оператору
    operators = ["+", "-", "*", "/"]
    try:
        first = (token[1])
        second = (token[2])
        operator = str(token[0])
        assert operator in operators, f"Первый элемент выражения должен быть оператором {operators}"
        assert first.isdigit(), "Второй элемент выражения должен быть числом"
        assert first.isdigit(), "Третий элемент выражения должен быть числом"
        if operator in operators:
            if operator == "+":
                result = int(first) + int(second)
                print(result)
            elif operator == "-":
                result = int(first) - int(second)
                print(result)
            elif operator == "/":
                try:
                    result = int(first) / int(second)
                    print(result)
                except ZeroDivisionError:
                    print(f"Произошла ошибка, делить на {second} нельзя")
            elif operator == "*":
                result = int(first) * int(second)
                print(result)
    except AssertionError as msg:
        print(msg)
    except IndexError:
        print("Элементы должны разделены пробелом ' '")


if __name__ == "__main__":
    while True:
        user_input = input("Введите выражение: ")
        polish(user_input)
