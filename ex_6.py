with open('file_for_ex_6.txt', encoding='utf-8') as file:
    for line in file:
        subject, lecture, practice, lab = line.split()

        res_l = ''
        res_p = ''
        res_lb = ''

        for el in lecture:
            if el == '(':
                break
            elif el == '—':
                el = '0'
            res_l += el
        for el in practice:
            if el == '(':
                break
            elif el == '—':
                el = '0'
            res_p += el
        for el in practice:
            if el == '(':
                break
            elif el == '—':
                el = '0'
            res_lb += el

        print(f'{subject} {int(res_l) + int(res_p) + int(res_lb)}')
