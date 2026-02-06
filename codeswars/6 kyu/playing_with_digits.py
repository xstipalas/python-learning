def dig_pow(n, p):
    total = sum(int(dig) ** i for i, dig in enumerate(str(n), start=p))
    
    total_div, total_mod = divmod(total, n)
    
    return total_div if total_mod == 0 else -1
