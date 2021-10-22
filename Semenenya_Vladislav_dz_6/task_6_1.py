import re

users = []
ip = []
tmp = set()
unique_ip = []

with open ('nginx_logs.txt', 'r', encoding='UTF-8') as file:
    for row in file:
        line = re.split('--|"| ', row)
        user = line[0], line[6], line[7]
        users.append(user)
        ip.append(line[0])

for i in ip:
    if i not in tmp:
        unique_ip.append(i)
        tmp.add(i)

counter = ip.count(unique_ip[0])
adress = unique_ip[0]
for i in unique_ip:
    if ip.count(i) > counter:
        counter = ip.count(i)
        adress = i

print(users)
print(f'Спамер: {adress}\nКоличество запросов: {counter}')