def recap_fun(argv):
    program, *arg = argv
    with open('bakery.csv', 'r', encoding='utf-8') as file:
        if len(sys.argv)-1 == 0:
            lines = file.readlines()
            for i in range(len(lines)):
                print(f'{str(i+1)} : {lines[i].strip()}')
        elif len(sys.argv)-1 == 1:
            lines = file.readlines()
            start = int(''.join(arg[0]))
            for i in range(start - 1, len(lines)):
                print(f'{str(i+1)} : {lines[i].strip()}')
        elif len(sys.argv)-1 == 2:
            lines = file.readlines()
            start = int(''.join(arg[0]))
            end = int(''.join([arg[1]]))
            if end <= len(lines):
                for i in range(start - 1, end):
                    print(f'{str(i+1)} : {lines[i].strip()}')
            else:
                for i in range(start-1, end):
                    print(f'{str(i+1)} : {lines[i].strip()}')


if __name__ == '__main__':
    import sys
    exit(recap_fun(sys.argv))
