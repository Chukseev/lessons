with open('file_for_ex_2.txt', encoding='utf-8') as file:
    content = file.readlines()
    print(f'Количество строк - {len(content)}')
    i = 1
    for el in content:
        print(f'Количество слов в {i} строке - {len(el.split(" "))}')
        i += 1