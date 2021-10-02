def sum_digits(value):
    result = 0

    while value != 0:
        result += value % 10
        value //= 10

    return result


numbers_lst = []

digit_first = 0
digit_second = 0

for i in range(1, 1001, 2):
    numbers_lst.append(i**3)

for i in range(len(numbers_lst)):
    if sum_digits(numbers_lst[i]) % 7 == 0:
        digit_first += numbers_lst[i]

for i in range(len(numbers_lst)):
    if sum_digits(numbers_lst[i]+17) % 7 == 0:
        digit_second += numbers_lst[i]

print(digit_first)
print(digit_second)
