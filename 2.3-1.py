#  Реализовать Польскую нотацию для двух положительных чисел.
def change_place(item):
    string_input = item
    token = string_input.split(" ")  # разделяем строку по пробелу, для обращения по индексу к числам и оператору
    operators = ["+", "-", "*", "/"]

    try:
        first = int(token[1])
        second = int(token[2])
        operator = str(token[0])
        if operator in operators:
            if operator == "+":
                result = first + second
                print(result)
            elif operator == "-":
                result = first - second
                print(result)
            elif operator == "/":
                try:
                    result = first / second
                    print(result)
                except ZeroDivisionError:
                    print(f"Произошла ошибка, делить на {second} нельзя")
            elif operator == "*":
                result = first * second
                print(result)
    except IndexError:
        print("Между числами и операторами должен быть пробел ' '")
    except ValueError:
        print(f"Выражение должно начинаться с операторов {operators}")


if __name__ == "__main__":
    user_input = input("Введите выражение: ")
    change_place(user_input)
