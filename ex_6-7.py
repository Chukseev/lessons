def int_func(text):
    return text.title()


my_list = input('--> ').split(' ')
new_list = []

for i in my_list:
    i = int_func(i)
    new_list.append(i)
    new_str = ' '.join(new_list)

print(new_str)
