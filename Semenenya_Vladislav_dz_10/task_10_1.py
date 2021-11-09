"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
| 31 22 |
| 37 43 |
| 51 86 |

| 3 5 32 |
| 2 4 6 |
| -1 64 -8 |

| 3 5 8 3 |
| 8 3 7 1 |
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц). Результатом
сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и пр.
"""


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self) -> str:
        ret = ''
        for row in self.matrix:
            ret += f'| {" ".join(map(str, row))} | \n'

        return ret

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError('Not Matrix')
        ret = []

        for row, other_row in zip(self.matrix, other.matrix):
            ret.append(list(map(sum, zip(row, other_row))))

        return Matrix(ret)


first_matrix = Matrix([[31, 32], [37, 43], [51, 86]])
second_matrix = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
third_matrix = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])

print(first_matrix)
print(second_matrix)
print(third_matrix)
