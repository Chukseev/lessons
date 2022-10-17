def my_func(num_1, num_2, num_3):
    my_numbers = [num_1, num_2, num_3]
    my_numbers.remove(min(my_numbers))
    result = my_numbers[0] + my_numbers[1]
    return result
num_1 = int(input('Введите первое число --> '))
num_2 = int(input('Введите второе число --> '))
num_3 = int(input('Введите третье число --> '))
print(f'Сумма двух наибольших чисел равна {my_func(num_1, num_2, num_3)}')