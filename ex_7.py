res_day = int(input('Какой результат пробежки составил первй день --> '))
purpose = int(input('Введите вашу цель --> '))
day = 1
while res_day < purpose:
    print(f'{day} день составил {round(res_day, 2)}')
    res_day = res_day + res_day / 10
    day += 1
print(f'{day} день составил {round(res_day, 2)}')
print(f'На {day} день спортсмен достиг результата — не менее {purpose} км.')
