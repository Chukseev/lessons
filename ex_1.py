with open("file_for_ex_1.txt", "w", encoding="utf-8") as file:
    print('Выход - enter')
    my_string = None
    while my_string != '':
        my_string = input('Введите данные --> ')
        file.write(my_string + '\n')




