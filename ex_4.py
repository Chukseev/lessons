def my_func_1(x, y):
    res = x ** y
    return res
def my_func_2(x, y):
    new_num = x
    for i in range(1, y):
        x = x * new_num
    return x
num_1 = int(input('Введите число --> '))
num_2 = int(input('Введите степень --> '))
print(my_func_1(num_1, num_2))
print(my_func_2(num_1, num_2))