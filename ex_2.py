def person_info(**kwargs):
    print(f"{kwargs['name']} {kwargs['lastname']} {kwargs['date_of_birthday']} {kwargs['city']} {kwargs['email']} {kwargs['phone']}")

person_info(name = 'Никита',
            lastname = 'Чуксеев',
            date_of_birthday = '31.12.2002',
            city = 'Москва',
            email = 'chukseev.nikita@yandex.ru',
            phone = '+79775121718')


