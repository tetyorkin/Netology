# -*- coding: utf-8 -*-
import os
from datetime import datetime

start_time = datetime.now()
hostname = 'mail.ru'
count = '12'
size = '1000'
cmd = f'ping {hostname} -l {size} -n {count}'

# Контекст менеджер HostPing
class HostPing:
    def __init__(self, commands):
        self.start_time = datetime.now()
        print(f"\nВремя начала работы контексного менеджера {self.start_time}")
        self.commands = os.system(commands)

    def __enter__(self):
        return self.commands

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = datetime.now()
        print(f"\nВремя завершения работы контекстного менеджера {self.end_time}")
        print(f'\nВремя выполнения менеджера контекса {(self.end_time - self.start_time).total_seconds()} секунд')


# Задача №2 вызов менеджера контекста и запись времени выполнения программы в файл и вывод в консоль
if __name__ == '__main__':
    with HostPing(cmd) as ping_c:
        file = open('result.txt', 'w', encoding='utf-8')
    end_time = datetime.now()
    string = f"\nВремя выполнения всей программы при отправке {count} пакетов размером {size} " \
             f"байт до узла {hostname} {(end_time - start_time).total_seconds()} секунд"
    file.write(string)
    file.close()
    print(string)
