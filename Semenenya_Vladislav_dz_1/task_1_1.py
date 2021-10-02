duration = int(input('Введите количество секунд: '))

seconds = duration % 60
minutes = duration // 60 % 60
hours = duration // 3600 % 24
days = duration // 86400

if (minutes == 0) and (hours == 0) and (days == 0):
    print('{} сек'.format(seconds))
elif (hours == 0) and (days == 0):
    print('{} мин, {} сек'.format(minutes, seconds))
elif days == 0:
    print('{} час, {} мин, {} сек'.format(hours, minutes, seconds))
else:
    print('{} дн, {} час, {} мин, {} сек.'.format(days, hours, minutes, seconds))
