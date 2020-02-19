import json


def read_file(file_name):
    with open(file_name, encoding='utf-8') as f:
        file_content = f.read()
        templates = json.loads(file_content)
        print(templates)


if __name__ == '__main__':
    read_file('newsafr.json')
