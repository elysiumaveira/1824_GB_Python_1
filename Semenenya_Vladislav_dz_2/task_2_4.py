from random import uniform


def price():
    if i != len(lst) - 1:
        print(f'{int(lst[i])} руб {int(round(lst[i] - int(lst[i]), 2) * 100)} коп', end=', ')
    else:
        print(f'{int(lst[i])} руб {int(round(lst[i] - int(lst[i]), 2) * 100)} коп')


lst = []

for i in range(20):
    lst.append(round(uniform(0, 100), 2))

for i in range(len(lst)):
    price()

lst.sort()

for i in range(len(lst)):
    price()

reversed_lst = []
lst.reverse()

for i in range(len(lst)):
    reversed_lst.append(lst[i])

print(reversed_lst)

print(reversed_lst[:5])
