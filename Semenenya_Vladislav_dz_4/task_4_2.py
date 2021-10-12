"""
Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API
можно использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос
к API в обычном браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить
поставленную задачу? Функция должна возвращать результат числового типа, например float. Подумайте: есть ли
смысл для работы с денежными величинами использовать вместо float тип Decimal? Сильно ли усложняется код
функции при этом? Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли
сделать работу функции не зависящей от того, в каком регистре был передан аргумент? В качестве примера
выведите курсы доллара и евро.
"""

import requests
import sys
import typing
from pyquery import PyQuery as pq
from lxml import etree

URL = 'http://www.cbr.ru/scripts/XML_daily.asp'


def send_request() -> requests.Response:
    """
    Выполняет запрос в банк
    """

    response = requests.get(URL)

    if not response.ok:
        print(f'Запрос не успешен: {response.status_code}')
        sys.exit(0)

    return response


def extract_data(tag: str) -> typing.List:
    """
    Извлекает данные из соответствующего тега и возвращает список string значений
    """

    res = send_request()
    main_root = pq(etree.fromstring(res.content))
    curs_val = main_root.pop()
    return curs_val.xpath(f'//Valute/{tag}/text()')


def currency_rates(code) -> float:
    char_code_currency = extract_data('CharCode')
    value_currency = extract_data('Value')

    for i in range(len(char_code_currency) - 1):
        if code == char_code_currency[i]:

            digit = str(value_currency[i]).split(',')

            return float(f'{digit[0]}.{digit[1]}')

if __name__ == '__main__':
    currency = input('Введите валюту: ')
    print(currency_rates(currency))
