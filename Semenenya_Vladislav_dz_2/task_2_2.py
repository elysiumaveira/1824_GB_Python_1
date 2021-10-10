def get_sign(x):  # функция для определения +/-
    if x[0] in '+-':
        return x[0]


arr = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0
while i < len(arr):
    sign = get_sign(arr[i])
    if arr[i].isdigit() or (sign and arr[i][1:].isdigit()):
        # если элемент число или эелемент содержит +/- и является числом
        if sign:  # если элемент содержит +/-
            arr[i] = sign + arr[i][1:].zfill(2)  # добавляем 0 к числу
        else:  # иначе
            arr[i] = arr[i].zfill(2)  # добавляем 0 к числу

        arr.insert(i, '"')  # добавляем " "
        arr.insert(i + 2, '"')  # добавляем " "
        i += 2

    i += 1

for i in range(len(arr)):
    elem = arr[i]
    past_elem = arr[i-1]
    if i == len(arr)-1:
        next_elem = None
    else:
        next_elem = arr[i+1]

    if (elem == '"') and (next_elem.isdigit() or get_sign(next_elem)) :
        print(arr[i], end='')
    elif i == len(arr) - 3:
        print(arr[i], end='')
    elif elem.isdigit():
        print(arr[i], end='')
    else:
        print(arr[i], end=' ')
