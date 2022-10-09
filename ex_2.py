my_list = []
my_element = None
i = 0
print('Выход из команды --> Exit')
while my_element != 'Exit':
    my_element = input('Введите элемент для списка --> ')
    if my_element == 'Exit':
        break
    my_element_2 = input('Введите элемент для списка --> ')
    if my_element_2 == 'Exit':
        break
    else:
        my_list.append(my_element_2)
        my_list.append(my_element)

print(my_list)
