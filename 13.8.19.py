num = int(input('Сколько билетов вы хотите приобрести:'))
cost = 0.0
for i in range(num):
    age = int(input('Возраст посетителя:'))
    if age < 18:
        cost = cost + 0
    elif 18 <= age < 25:
        cost = cost + 990
    else:
        cost = cost + 1390
    if num > 3:
        cost = cost * 0.9
print('Итого:' + ' ' + str(round(cost)) + ' ' + 'рублей')