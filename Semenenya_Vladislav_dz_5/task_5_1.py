"""
Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
#>>> odd_to_15 = odd_nums(15)
#>>> next(odd_to_15)
1
#>>> next(odd_to_15)
3
...
#>>> next(odd_to_15)
15
#>>> next(odd_to_15)
#...StopIteration...
"""


def odd_nums(n):
    for num in range(1, n, 2):
        yield num


generator_length = int(input('Введите длину генератора: '))

print(*odd_nums(generator_length))

# odd_to_n = odd_nums(generator_length)
#
# for _ in range(generator_length):
#     print(next(odd_to_n))

print(type(odd_nums(generator_length)))
