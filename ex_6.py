my_list = []
my_list_all = []
i = 1
command = None
while command != 'Выход':
    command = input('Нажмите любую клавишу для продолжения \nЧто бы выйти из программы напишите - "Выход" \n--> ')
    if command == 'Выход':
        break
    else:
        name = input(f'Введите название {i}-го товара--> ')
        price = int(input(f'Введите цену {i}-го товара--> '))
        quantity = int(input(f'Введите количество {i}-го товара--> '))
        unit = input(f'Введите ед. {i}-го товара-->')
        my_list = (i, {'название': [name],'цена': [price],'количество': [quantity],'ед.': [unit]})
        my_list_all.append(my_list)
    i += 1
print(my_list_all)
print(i)
j = 0
while j != len(my_list_all):
    print(my_list_all[j])
    j += 1




