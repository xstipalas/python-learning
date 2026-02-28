# С помощью замыкания можно создавать функции с запоминанием значений
def create_user():
    user_id = 0

    def get_id(name):
        nonlocal user_id

        user_id += 1

        print(f'Создан пользователь {name} с идентификатором: {user_id:06}')

    return get_id

create = create_user()

create('Максим')
create('Оля')
create('Саша')

def mod(m): return lambda n: n % m

mod_five = mod(5)

print(f'\n1 mod 5 = {mod_five(1)}')
print(f'7 mod 5 = {mod_five(7)}')
print(f'15 mod 5 = {mod_five(15)}')