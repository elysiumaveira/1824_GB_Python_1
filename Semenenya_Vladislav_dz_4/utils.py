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
    res = send_request()
    main_root = pq(etree.fromstring(res.content))
    curs_val = main_root.pop()

    char_code_currency = extract_data('CharCode')
    value_currency = extract_data('Value')

    for i in range(len(char_code_currency) - 1):
        if code == char_code_currency[i]:

            digit = str(value_currency[i]).split(',')
            float_digit = float(f'{digit[0]}.{digit[1]}')
            date = curs_val.attrib["Date"]
            print(f'{float_digit}, {date}')
            return float_digit