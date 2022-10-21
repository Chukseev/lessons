def fact(n):
    res = 1
    for el in range(1, n + 1):
        res = el * res
        yield res
number_one = fact(5)
for el in fact(5):
    print(el)
