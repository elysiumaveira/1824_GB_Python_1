"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
завершиться с ошибкой.
"""


class Division:
    def __init__(self, divider: int, denominator: int):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide(divider, denominator):
        try:
            return (divider / denominator)
        except ZeroDivisionError as ve:
            return f'ошибка {ve}'


division = Division
print(division.divide(10, 0), '\n')
print(division.divide(100, 10))
