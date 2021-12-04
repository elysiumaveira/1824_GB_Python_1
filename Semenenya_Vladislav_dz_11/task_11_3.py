"""
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо
только числами. Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
скрипта, введя, например, команду «stop». При этом скрипт завершается, сформированный список с числами выводится на
экран.
"""


class NotNumber(ValueError):
    pass

    def checker(self):
        my_list = []
        while True:
            try:
                print('Введите q для выхода. \n')
                value = input('Введите занчение: ')

                if value == 'q':
                    print('Программа остановлена...')
                    break
                if not value.isdigit():
                    raise NotNumber(value)
                my_list.append(int(value))
            except NotNumber as ex:
                print(f'{ex} не является числом')
            print(my_list)


NotNumber.checker(1)
