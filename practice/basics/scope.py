a, b, c, d, e = 1, 2, 3, 4, 5

def output():
    global b

    a, b = 2, 3
    c, d = 4, 5

    def output2():
        nonlocal d

        c, d = 5, 6
        e = 7

        print(f'Значения при output2: a = {a}, b = {b}, c = {c}, d = {d}, e = {e}')

    print(f'Значения при output: a = {a}, b = {b}, c = {c}, d = {d}, e = {e}')
    output2()
    print(f'Значения после output2: a = {a}, b = {b}, c = {c}, d = {d}, e = {e}')

print(f'Начальные значения: a = {a}, b = {b}, c = {c}, d = {d}, e = {e}')
output()
print(f'Итоговые значения: a = {a}, b = {b}, c = {c}, d = {d}, e = {e}')
