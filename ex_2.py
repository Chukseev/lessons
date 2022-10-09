number = int(input('Введите количество секунд --> '))
seconds = number % 60
minutes = number % 3600 // 60
hours = number // 3600
print('Получилось что: ')
print(f'{hours}:{minutes}:{seconds}')

