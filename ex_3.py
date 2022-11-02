with open('file_for_ex_3.txt', encoding='utf-8') as file:
    content = file.read().split('\n')
    poor_people = []
    sum_salary = []
    # poor_people = [i[0] for i in content if int(i[1]) < 20000]
    for i in content:
        el = i.split()
        if float(el[1]) < 20000:
            poor_people.append(el[0])
        sum_salary.append(float(el[1]))
    print(f'Зарплату ниже 20000р имеют {poor_people}\n'
          f'Средняя зарплата составляет {round(sum(sum_salary) / len(sum_salary), 2)}')
