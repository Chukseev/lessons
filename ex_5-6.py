revenue = int(input('Введите выручку фирмы--> '))
cost = int(input('Введите издержку фирмы--> '))
if revenue > cost:
    res = revenue - cost
    print(f'Прибыль вашей фирмы составляет {res} р.')
    staff = int(input('Введите кодичество сотрудников--> '))
    print(f'Прибыль в расчёте на одного сотрудника состовляет {res / staff} р.')

elif revenue < cost:
    res = cost - revenue
    print(f'Убыток вашей фирмы составляет {res} р.')

else:
    print('Вы вышли в ноль')