def square_digits(num):
    return int(''.join(str(int(dig) ** 2) for dig in str(num)))