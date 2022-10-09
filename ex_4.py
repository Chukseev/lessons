max_num = 0
number = int(input('Введите число --> '))

while number > 1:
    print(number)
    if number % 10 > max_num:
        max_num = number % 10
    number = number // 10

print(f'Максимальное число --> {max_num}')