def digital_root(n: int) -> int:
    return n if n < 10 else digital_root(sum(map(int, str(n))))