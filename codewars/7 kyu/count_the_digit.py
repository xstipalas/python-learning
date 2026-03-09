def nb_dig(n: int, d: int) -> int:
    d_str = str(d)
    return sum(str(num ** 2).count(d_str) for num in range(n + 1))