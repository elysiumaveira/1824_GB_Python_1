"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


from datetime import date


class Data:
    def __init__(self, data: str):
        self.data = data

    @classmethod
    def extract(cls, data):
        try:
            day, month, year = [int(i) for i in data.split('-')]
            return day, month, year
        except ValueError:
            return 'Указана неверная дата'

    @staticmethod
    def valid(data):
        try:
            day, month, year = data.split('-')
            date(int(year), int(month), int(day))
            return 'Дата введена верно'
        except ValueError:
            return 'Указана неверная дата'


print(Data.valid('09-02-2021'))
print(Data.extract('25-03'))
