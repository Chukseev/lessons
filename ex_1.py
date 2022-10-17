def my_division(num_1, num_2):
    result = num_1 / num_2
    return result

try:
    number_1 = int(input('Введите делитель --> '))
    number_2 = int(input('Введите делимое --> '))
    print(my_division(number_1, number_2))
except ZeroDivisionError:
    print('На ноль делить нельзя!')