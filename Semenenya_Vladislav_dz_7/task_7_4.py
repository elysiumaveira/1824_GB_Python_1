"""
Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница
размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках), размер
которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
"""


import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
folder = os.path.join(BASE_DIR, 'some_folder')


def size_of_files(path: str):
    data = []
    for d in os.walk(path):
        for file in d[2]:
            _, ex = file.split('.')
            data.append([os.stat('/'.join(data[0], file)).st_size, ex])

    return data


def counter(path):
    dictionary = {

    }

    for item in size_of_files(path):
        count = 10
        while True:
            if item[0] < count:
                if count in dictionary:
                    dictionary[count] += 1
                else:
                    dictionary[count] = 1
                break
            count *= 10

    return dictionary


print(counter(folder))
