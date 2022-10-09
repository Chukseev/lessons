my_string = input('Введите слова через пробел --> ')
new_string = my_string.split(' ')
num = 1
for i in new_string:
    print(f'{num} слово - {i[:10]}')
    num += 1