with open('file_for_ex_5.txt', 'w', encoding='utf-8') as file:
    my_numbers = input('Введите числа разделенные пробелом --> ')
    file.write(my_numbers)
with open('file_for_ex_5.txt', encoding='utf-8') as file:
    result = file.read().split(' ')
    new_result = 0
    for el in result:
        new_result += int(el)
    print(new_result)