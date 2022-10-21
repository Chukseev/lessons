from itertools import count
from itertools import cycle

for el in count(3):
    if el == 10:
        break
    print(el)
i = 0
end_i = int(input('Введите число --> '))
for el in cycle('ABC'):
    if i > end_i:
        break
    print(el)
    i += 1

