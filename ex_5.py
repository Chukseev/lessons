def my_sum(general_sum = 0):
    my_list = input('--> ').split(' ')
    for i in range(len(my_list)):
        if my_list[i] != 'q':
            general_sum = general_sum + int(my_list[i])

        else:
            break
    print(general_sum)
    if 'q' in my_list:
        exit('выход')
    else:
        my_sum(general_sum)

print(my_sum())