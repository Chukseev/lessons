import json

with open('file_for_ex_7.txt', encoding='utf-8') as file:
    my_dict = {}
    my_dict_2 = {}
    average_profit = 0
    for content in file:
        name_firm, num, revenue, cost = content.split(' ')
        new_cost = ''
        for el in cost:
            if el == '.':
                break
            new_cost += el

        res = int(revenue) - int(new_cost) # прибыль
        average_profit += res
        my_dict[name_firm] = res # добавляем в словарь

    my_dict_2['average_profit'] = average_profit / len(my_dict)
    my_list = [my_dict, my_dict_2]
    print(my_list)
    with open('file_for_ex_7.json', 'w', encoding='utf-8') as file:
        json.dump(my_list, file)