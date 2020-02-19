import json


def read_file(file_name):
    with open(file_name, encoding='utf-8') as f:
        file_content = f.read()
        templates = json.loads(file_content)
        new = templates['rss']['channel']['items']
        big_world = []
        for key in new:
            item = key['description'].split()
            for word in item:
                if len(word) > 6:
                    big_world.append(word.lower().split())
        big_world_sorted = sorted(big_world)


if __name__ == '__main__':
    read_file('newsafr.json')
