exclusions = {11, 12, 13, 14, 15}

for i in range(100):
    if i in exclusions:
        print(i, "процентов")
    elif i % 10 == 1:
        print(i, "процент")
    elif (i % 10) > 1 and (i % 10 < 5):
        print(i, "процента")
    else:
        print(i, "процентов")
