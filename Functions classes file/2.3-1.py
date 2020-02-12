#  Реализовать Польскую нотацию для двух положительных чисел.
def polish(string_input):
    token = string_input.split()  # разделяем строку по пробелу, для обращения по индексу к числам и оператору
    operators = ["+", "-", "*", "/"]
    if len(token) > 3:
        print("Введено больше аргументов, необходимо ввести в формате 'оператор число1 число2'")
    else:
        try:
            operator = str(token[0])
            assert operator in operators, f"Первый аргумент выражения должен быть оператором {operators}"
            first = int(token[1])
            second = int(token[2])
            if operator == "+":
                result = first + second
                print(result)
            elif operator == "-":
                result = first - second
                print(result)
            elif operator == "/":
                result = first / second
                print(result)
            elif operator == "*":
                result = first * second
                print(result)
        except AssertionError as msg:
            print(msg)
        except IndexError:
            print("Передано не допустимое количество аргументов")
        except ZeroDivisionError:
            print("Произошла ошибка, делить на 0 нельзя")
        except ValueError:
            print("Операции допустимы только с числами")


if __name__ == "__main__":
    while True:
        user_input = input("Введите выражение: ")
        polish(user_input)
