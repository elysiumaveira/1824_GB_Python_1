lst = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

some_str = ''

i = 0

for elem in lst:
    some_str = elem
    lst[i] = some_str.split()
    some_str = ''
    i += 1

for i in lst:
    for j in range(len(i)):
        if j == len(i)-1:
            some_str = i[j]
            name = some_str.capitalize()
            print(f'Привет, {name}!')
