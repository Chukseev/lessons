my_numbers = {'One' : 'Один',
              'Two' : 'Два',
              'Three' : 'Три',
              'Four' : 'Четыре',
              'Five': 'Пять',
              'Six': 'Шесть',
              'Seven': 'Семь',
              'Eight': 'Восемь',
              'Nine': 'Девять'}
with open('file_for_ex_4.txt', encoding='utf-8') as file:
    content = file.read().split('\n')
    result = []
    for el in content:
        el = el.split(' — ')
        el[0] = my_numbers[el[0]]
        result.append(el)
print(result)
with open('new_file_for_ex_4.txt', 'w', encoding='utf-8') as file:
    new_res = []
    for el in result:
        new_res.append(' — '.join(el))
    content = file.write('\n'.join(new_res))


