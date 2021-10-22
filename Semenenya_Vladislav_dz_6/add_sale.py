def enter_fun(argv):
    program, *arg = argv
    arg_str = ','.join(arg)
    with open('bakery.csv', 'a', encoding='utf=8') as file:
        file.write(f'{arg_str}\n')


if __name__ == '__main__':
    import sys

    exit(enter_fun(sys.argv))
