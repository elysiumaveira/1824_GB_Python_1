with open('users.csv', encoding='UTF-8') as users_file:
    users_line = [i.strip() for i in users_file]
    with open('hobby.csv', encoding='UTF-8') as hobby_file:
        hobby_line = [j.strip() for j in hobby_file]
        my_dict = dict(zip(users_line, hobby_line))
        if len(users_line) > len(hobby_line):
            new_dict = dict.fromkeys(users_line[len(hobby_line):], None)
            my_dict.update(new_dict)
        elif len(users_line) < len(hobby_line):
            print(str(f'Хобби ({len(hobby_line)}) больше, чем людей ({len(users_line)})'))
        else:
            my_dict = dict(zip(users_line, hobby_line))

print(my_dict)
