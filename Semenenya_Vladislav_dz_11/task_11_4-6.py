"""
------------------------------------------------------------------------------------------------------------------------

Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
уникальные для каждого типа оргтехники.

------------------------------------------------------------------------------------------------------------------------

Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в
определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру (например, словарь).

------------------------------------------------------------------------------------------------------------------------

Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

------------------------------------------------------------------------------------------------------------------------
"""


class Warehouse:
    """Класс склада оргтехники"""
    # Объявление необходимых атрибутов класса
    _content = {'Printer': 0,
                'Scanner': 0,
                'Xerox': 0}
    _maxcapasity = 0

    def __init__(self, maxcapasity: int):
        self._maxcapasity = maxcapasity

    def add_item(self, cls):
        """Метод добавления коробки на склад"""
        self.part_add(cls.title, cls.quantity)

    def remove_item(self, param_1: str, param_2: int):
        """Метод для выдачи со склада"""
        if type(param_1) is not str or type(param_2) is not int:
            msg = f'Не верный тип данных {param_1} или {param_2}. Должно быть param_1 - строка, param_2 - целое число.'
            raise ValueError(msg)
        else:
            if param_1.capitalize() in self._content.keys():
                if self._content[param_1] >= param_2:
                    a = self._content[param_1] - param_2
                    self._content[param_1] = a
                else:
                    msg = f'{param_1} нет на складе в достаточном количестве'
                    raise Exception(msg)
            else:
                msg = f'Техники с названием {param_1} нет на складе'
                raise Exception(msg)

    @staticmethod
    def part_add(param_1: str, param_2: int):
        """Метод для добавления на склад части коробки с техникой"""
        if (sum(Warehouse._content.values()) + param_2) >= Warehouse._maxcapasity:
            a = Warehouse._content[param_1] + param_2
            Warehouse._content[param_1] = a
        else:
            msg = f'Я не могу поместить это на склад. Количество {param_1} в размере {param_2} слишком большое'
            raise Exception(msg)

    def __str__(self):
        """Отчетность для контроля того что есть на складе"""
        return f'{self._content}'


class OfficeEq:
    """Класс оргтехники"""
    def __init__(self, title: str, color: str):
        self.title = title
        self.color = color

    def move_to_warehouse(self, par: int):
        """перемещение на склад части коробки"""
        if type(par) is int:
            if self.quantity >= par:
                self.quantity = self.quantity - par
                Warehouse.part_add(self.title, par)
            else:
                msg = f'Я не могу переместить {self.title} в количестве {par} на склад, т.к. в коробке их столько нет'
                raise Exception(msg)
        else:
            msg = f'Необходимо указыать перемещаемое кол-во как int, а не {type(par)}'
            raise Exception(msg)

    def __str__(self):
        """Перегрузка строкового метода для контроля того что осталось в коробке"""
        return f'{self.quantity}'


class Printer(OfficeEq):
    def __init__(self, seal: bool, quantity: int):
        self.seal = seal
        self.quantity = quantity
        OfficeEq.__init__(self, title='Printer', color='белый')


class Scanner(OfficeEq):
    def __init__(self, scanning: bool, quantity: int):
        self.scanning = scanning
        self.quantity = quantity
        OfficeEq.__init__(self, title='Scanner', color='черный')


class Xerox(OfficeEq):
    def __init__(self, what_we_copy: str, quantity: int):
        self.what_we_copy = what_we_copy
        self.quantity = quantity
        OfficeEq.__init__(self, title='Xerox', color='красный')


try:
    xerox = Xerox('бззз', 1)
    printer = Printer(False, 3)
    scanner = Scanner(True, 2)
    warehouse = Warehouse(10)

    warehouse.add_item(xerox)
    warehouse.add_item(printer)
    warehouse.add_item(scanner)

    print(warehouse)

    printer1 = Printer(False, 5)

    printer1.move_to_warehouse(2)

    print(warehouse)

    warehouse.remove_item('Scanner', 1)
    print(warehouse)
except Exception as error:
    print(error)
except ValueError as error:
    print(error)
