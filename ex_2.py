# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

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
