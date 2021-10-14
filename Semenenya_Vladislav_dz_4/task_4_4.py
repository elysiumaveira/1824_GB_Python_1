"""
Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания. Создать скрипт,
в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates(). Убедиться, что ничего
лишнего не происходит.
"""

from utils import currency_rates

if __name__ == '__main__':
    for i in range(int(input('Введите количество повторений: '))):
        currency = input('Введите валюту: ')
        currency_rates(currency)
