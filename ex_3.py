mounth = int(input('Введите месяц от 1 до 12 -->'))
list_mounth = ['Зима', 'Весна', 'Лето', 'Осень']
if mounth == 12 or mounth == 1 or mounth == 2:
    print(list_mounth[0])
if mounth == 3 or mounth == 4 or mounth == 5:
    print(list_mounth[1])
if mounth == 6 or mounth == 7 or mounth == 8:
    print(list_mounth[2])
if mounth == 9 or mounth == 10 or mounth == 11:
    print(list_mounth[3])
dict_mounth = {
    12: 'Зима',
    1: 'Зима',
    2: 'Зима',
    3: 'Весна',
    4: 'Весна',
    5: 'Весна',
    6: 'Лето',
    7: 'Лето',
    8: 'Лето',
    9: 'Осень',
    10: 'Осень',
    11: 'Осень'
}
print(dict_mounth[mounth])
