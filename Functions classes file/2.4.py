import re
def open_file(name_file):
    regex = re.compile(r"(?P<head>^.+\n(?P<id>\d))", re.MULTILINE)
    with open(name_file, encoding='utf8') as file:
        for match in regex.finditer(file.read()):
            r = []
            r += [{match.group('head'): match.group('head')}]


            print(r)



if __name__ == "__main__":
    open_file('recipes.txt')
