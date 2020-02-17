import re


def make_cook_book(name_file):
    regex = re.compile(r"(?P<head>^.+\n(?P<id>\d))", re.MULTILINE)
    with open(name_file, encoding='utf8') as file:
        for match in regex.finditer(file.read()):
            r = []
            r += [{match.group('head'): match.group('head')}]


if __name__ == "__main__":
    make_cook_book('recipes.txt')
