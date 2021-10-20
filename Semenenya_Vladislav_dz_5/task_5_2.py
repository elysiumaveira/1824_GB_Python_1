"""
(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
"""

generator_length = int(input('Введите длину генератора: '))

odd_nums = (num for num in range(1, generator_length, 2))

print(*odd_nums)
print(type(odd_nums))
