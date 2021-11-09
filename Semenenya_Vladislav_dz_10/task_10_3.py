"""
Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс «Клетка».
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны
быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение
(__mul__()), деление (__floordiv__, __truediv__()). Эти методы должны применяться только к клеткам и выполнять
увеличение, уменьшение, умножение и округление до целого числа деления клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если разность количества ячеек двух клеток
больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение количества ячеек этих двух клеток.
Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Этот метод
позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5. В этом случае метод make_order() вернёт
строку: *****\n*****\n**.
"""


class Cell:
    def checker(self, other):
        if not isinstance(other, Cell):
            raise TypeError(f'{other} not a Cell class')

    def __init__(self, cell_numbers: int):
        self.cells = cell_numbers

    def __str__(self):
        return f'в данной клетке: {self.cells} ячеек'

    def __add__(self, other):
        self.checker(other)
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        self.checker(other)
        if not self.cells - other.cells > 0:
            print('разность клеток 0 или меньше')
        return Cell(self.cells - other.cells)

    def __mul__(self, other):
        self.checker(other)
        return Cell(self.cells + other.cells)

    def __floordiv__(self, other):
        self.checker(other)
        return Cell(self.cells // other.cells)

    def __truediv__(self, other):
        self.checker(other)
        return Cell(int(self.cells / other.cells))

    def make_order(self, n):
        lines = self.cells // n
        rest = self.cells % n
        result = ''
        for i in range(lines):
            result += f'{"*" * n}\n'
        result += f'{"*" * n}\n'

        return result


cell = Cell(15)
cell_1 = Cell(10)
cell_2 = Cell(3)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1 // cell_2)
print(cell.make_order(5))
